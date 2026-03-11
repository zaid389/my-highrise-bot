from flask import Flask, render_template, jsonify, request, redirect, url_for
import json
import os
import time
from threading import Thread
from datetime import datetime
import requests

# إنشاء تطبيق Flask
app = Flask(__name__)

# متغيرات البوت العامة
bot_instance = None

# إعدادات الاتصال بـ Replit
REPLIT_BOT_URL = "https://highrise-bot-system-vector000.replit.app"  # ضع URL Replit هنا
API_KEY = "REPLIT_BOT_API_KEY_2024"

class ReplitBotConnector:
    """مدير الاتصال بالبوت على Replit"""
    def __init__(self):
        self.base_url = REPLIT_BOT_URL
        self.api_key = API_KEY
        self.headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json'
        }
        self.timeout = 10  # timeout للطلبات
    
    def get_status(self):
        """جلب حالة البوت من Replit (Endpoint عام)"""
        try:
            response = requests.get(
                f"{self.base_url}/api/bot-status.json",
                timeout=self.timeout
            )
            if response.status_code == 200:
                return response.json()
            else:
                return {'success': False, 'error': f'HTTP {response.status_code}'}
        except requests.RequestException as e:
            return {'success': False, 'error': f'Connection error: {str(e)}'}
    
    def get_users(self):
        """جلب المستخدمين من Replit (Endpoint عام)"""
        try:
            response = requests.get(
                f"{self.base_url}/api/bot-users.json",
                timeout=self.timeout
            )
            if response.status_code == 200:
                return response.json()
            else:
                return {'success': False, 'error': f'HTTP {response.status_code}'}
        except requests.RequestException as e:
            return {'success': False, 'error': f'Connection error: {str(e)}'}
    
    def get_emotes(self):
        """جلب الرقصات من Replit (Endpoint عام)"""
        try:
            response = requests.get(
                f"{self.base_url}/api/bot-emotes.json",
                timeout=self.timeout
            )
            if response.status_code == 200:
                return response.json()
            else:
                return {'success': False, 'error': f'HTTP {response.status_code}'}
        except requests.RequestException as e:
            return {'success': False, 'error': f'Connection error: {str(e)}'}
    
    def execute_command(self, command):
        """إرسال أمر إلى البوت على Replit"""
        try:
            # محاولة استخدام API المحمي أولاً
            response = requests.post(
                f"{self.base_url}/remote/command",
                headers=self.headers,
                json={'command': command},
                timeout=self.timeout
            )
            if response.status_code == 200:
                return response.json()
            else:
                # إذا فشل، استخدم ملف مؤقت
                print(f"Failed to send command via API: {response.status_code}")
                return {'success': False, 'error': f'Command API failed: HTTP {response.status_code}'}
        except requests.RequestException as e:
            return {'success': False, 'error': f'Connection error: {str(e)}'}

# إنشاء مدير الاتصال بـ Replit
replit_connector = ReplitBotConnector()

# نظام fallback للبيانات الافتراضية
class FallbackData:
    """بيانات احتياطية عند فشل الاتصال بـ Replit"""
    @staticmethod
    def get_default_users():
        return [
            {
                "id": "657a06ae5f8a5ec3ff16ec1b",
                "username": "البوت",
                "user_type": "بوت",
                "is_active": True,
                "last_seen": datetime.now().isoformat()
            }
        ]
    
    @staticmethod
    def get_default_emotes():
        return ["emote-superpose", "emote-frog", "dance-tiktok10", "dance-weird", "idle-fighter"]

@app.route('/')
def index() -> str:
    return render_template('index.html')

@app.route('/outfits')
def outfits():
    return render_template('outfits.html')

@app.route('/updates')
def updates():
    return render_template('updates.html')

@app.route('/api')
def api_info():
    """معلومات أساسية عن API"""
    return jsonify({
        'name': 'Highrise Bot API',
        'version': '1.0.0',
        'status': 'running',
        'endpoints': [
            '/api/status',
            '/api/emotes', 
            '/api/users',
            '/api/room-users',
            '/api/execute-command'
        ],
        'success': True
    })

@app.route('/api/status')
def api_status():
    """جلب حالة البوت من Replit"""
    try:
        # الاتصال بـ Replit لجلب الحالة الفعلية
        replit_response = replit_connector.get_status()
        
        if replit_response.get('success'):
            status_data = replit_response.get('status', {})
            is_connected = replit_response.get('is_connected', False)
            
            return jsonify({
                'message': f"متصل مع Replit - {replit_response.get('message', 'Unknown status')}",
                'status': status_data,
                'success': is_connected,
                'note': 'البيانات مباشرة من Replit',
                'connection_source': 'replit'
            })
        else:
            # فشل الاتصال مع Replit - استخدم البيانات الافتراضية
            fallback_status = {
                'web_server': True,
                'bot_connected': False,
                'highrise_connection': False,
                'room_users_count': 1,
                'timestamp': time.time(),
                'room_id': None,
                'user_id': None,
                'connection_time': None,
                'source': 'fallback'
            }
            
            return jsonify({
                'message': f'فشل الاتصال مع Replit: {replit_response.get("error", "Unknown error")}',
                'status': fallback_status,
                'success': False,
                'note': 'البيانات الافتراضية - لا يمكن الوصول للبوت',
                'connection_source': 'fallback',
                'replit_error': replit_response.get('error')
            })
            
    except Exception as e:
        # خطأ في النظام
        return jsonify({
            'message': 'خطأ في النظام',
            'status': {'error': str(e)},
            'success': False,
            'note': 'خطأ في واجهة الويب'
        }), 500

@app.route('/api/users')
def get_users():
    """API للحصول على المستخدمين من Replit"""
    try:
        # الاتصال بـ Replit لجلب المستخدمين
        replit_response = replit_connector.get_users()
        
        if replit_response.get('success'):
            return jsonify({
                'success': True,
                'users': replit_response.get('users', []),
                'total_count': replit_response.get('total_count', 0),
                'source': 'replit'
            })
        else:
            # فشل الاتصال - استخدم البيانات الافتراضية
            default_users = FallbackData.get_default_users()
            return jsonify({
                'success': False,
                'users': default_users,
                'total_count': len(default_users),
                'source': 'fallback',
                'error': replit_response.get('error', 'Connection failed')
            })
            
    except Exception as e:
        # خطأ في النظام
        default_users = FallbackData.get_default_users()
        return jsonify({
            'success': False, 
            'users': default_users,
            'total_count': len(default_users),
            'source': 'fallback',
            'error': str(e)
        })

@app.route('/api/room-users')
def get_room_users():
    """API للحصول على مستخدمي الغرفة الحاليين"""
    try:
        # محاولة قراءة من ملف مؤقت
        room_users = []
        
        if os.path.exists('current_room_users.json'):
            with open('current_room_users.json', 'r', encoding='utf-8') as f:
                room_users = json.load(f)
        else:
            # بيانات افتراضية
            room_users = [
                {
                    "id": "657a06ae5f8a5ec3ff16ec1b",
                    "username": "البوت",
                    "position": {"x": 10, "y": 0, "z": 10}
                }
            ]

        return jsonify({
            'success': True,
            'users': room_users,
            'count': len(room_users),
            'source': 'files'
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e), 'users': []})

@app.route('/api/emotes')
def get_emotes():
    """API لجلب قائمة الرقصات من Replit"""
    try:
        # الاتصال بـ Replit لجلب الرقصات
        replit_response = replit_connector.get_emotes()
        
        if replit_response.get('success'):
            emotes_list = replit_response.get('emotes_list', [])
            return jsonify({
                "success": True,
                "emotes": emotes_list,
                "emotes_list": emotes_list,
                "total_emotes": len(emotes_list),
                "source": "replit"
            })
        else:
            # فشل الاتصال - استخدم البيانات الافتراضية
            default_emotes = FallbackData.get_default_emotes()
            return jsonify({
                "success": False,
                "emotes": default_emotes,
                "emotes_list": default_emotes,
                "total_emotes": len(default_emotes),
                "source": "fallback",
                "error": replit_response.get('error', 'Connection failed')
            })

    except Exception as e:
        # خطأ في النظام
        default_emotes = FallbackData.get_default_emotes()
        return jsonify({
            "success": False,
            "error": f"فشل في تحميل بيانات الرقصات: {str(e)}",
            "emotes": default_emotes,
            "emotes_list": default_emotes,
            "source": "fallback"
        })

@app.route('/api/execute-command', methods=['POST'])
def execute_command():
    """API لتنفيذ الأوامر عبر Replit"""
    try:
        data = request.get_json()
        command = data.get('command', '').strip()
        
        if not command:
            return jsonify({'success': False, 'error': 'الأمر فارغ'})

        # إرسال الأمر إلى Replit
        replit_response = replit_connector.execute_command(command)
        
        if replit_response.get('success'):
            return jsonify({
                'success': True,
                'message': f'تم إرسال الأمر إلى البوت: {command}',
                'command': command,
                'source': 'replit',
                'timestamp': replit_response.get('timestamp')
            })
        else:
            return jsonify({
                'success': False,
                'error': f'فشل في إرسال الأمر: {replit_response.get("error", "Unknown error")}',
                'command': command,
                'source': 'replit_failed'
            })
    
    except Exception as e:
        return jsonify({
            'success': False, 
            'error': f'خطأ في النظام: {str(e)}',
            'source': 'system_error'
        })

@app.route('/api/emote-timing')
def get_emote_timing():
    """API لجلب توقيتات الرقصات"""
    try:
        timing_data = {}
        
        if os.path.exists('data/emote_timing.json'):
            with open('data/emote_timing.json', 'r', encoding='utf-8') as f:
                timing_data = json.load(f)
        
        return jsonify({
            'success': True,
            'timing': timing_data,
            'count': len(timing_data)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e), 'timing': {}})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)