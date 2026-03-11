
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔐 محمل الملفات الخفية لفريق EDX
يتعامل مع تحميل وإدارة الملفات المحمية بشكل آمن
"""

import os
import sys
import json
import importlib.util
from typing import Dict, Any, Optional

class EDXHiddenLoader:
    def __init__(self):
        self.hidden_files = {
            "secure_config": ".edx_team_secure",
            "env_vars": ".env_edx",
            "permissions": ".edx_permissions",
            "access_log": ".edx_access_log"
        }
        self.loaded_data = {}
        
    def load_hidden_config(self) -> Dict[str, Any]:
        """تحميل التكوين الخفي بأمان"""
        try:
            config_file = self.hidden_files["secure_config"]
            if os.path.exists(config_file):
                with open(config_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.loaded_data["secure_config"] = data
                    return data
            return {}
        except Exception as e:
            print(f"⚠️ خطأ في تحميل التكوين الخفي: {e}")
            return {}
    
    def load_env_vars(self) -> Dict[str, str]:
        """تحميل متغيرات البيئة الخفية"""
        try:
            env_file = self.hidden_files["env_vars"]
            if os.path.exists(env_file):
                env_vars = {}
                with open(env_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#') and '=' in line:
                            key, value = line.split('=', 1)
                            env_vars[key.strip()] = value.strip()
                            # إضافة إلى متغيرات البيئة الفعلية
                            os.environ[key.strip()] = value.strip()
                return env_vars
            return {}
        except Exception as e:
            print(f"⚠️ خطأ في تحميل متغيرات البيئة: {e}")
            return {}
    
    def load_permissions_module(self):
        """تحميل وحدة الصلاحيات الخفية"""
        try:
            permissions_file = self.hidden_files["permissions"]
            if os.path.exists(permissions_file):
                spec = importlib.util.spec_from_file_location("edx_permissions", permissions_file)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    return module
            return None
        except Exception as e:
            print(f"⚠️ خطأ في تحميل وحدة الصلاحيات: {e}")
            return None
    
    def verify_team_member(self, username: str) -> bool:
        """التحقق السريع من عضوية الفريق"""
        config = self.load_hidden_config()
        team_members = config.get("team_members", {})
        return any(member.upper() == username.upper() for member in team_members.keys())
    
    def get_member_data(self, username: str) -> Optional[Dict[str, Any]]:
        """الحصول على بيانات العضو الكاملة"""
        config = self.load_hidden_config()
        team_members = config.get("team_members", {})
        
        for member_name, member_data in team_members.items():
            if member_name.upper() == username.upper():
                return member_data
        return None
    
    def has_full_access(self, username: str) -> bool:
        """فحص الوصول الكامل"""
        member_data = self.get_member_data(username)
        if member_data:
            return (
                member_data.get("permissions") == "*" and
                member_data.get("bypass_all", False) and
                member_data.get("unlimited_access", False)
            )
        return False
    
    def initialize_hidden_system(self):
        """تهيئة النظام الخفي"""
        try:
            # تحميل جميع الملفات
            self.load_hidden_config()
            self.load_env_vars()
            permissions_module = self.load_permissions_module()
            
            print("🔐 تم تحميل النظام الخفي لفريق EDX بنجاح")
            print(f"📁 ملفات محملة: {len([f for f in self.hidden_files.values() if os.path.exists(f)])}")
            
            return True
        except Exception as e:
            print(f"❌ خطأ في تهيئة النظام الخفي: {e}")
            return False
    
    def create_access_report(self) -> str:
        """إنشاء تقرير الوصول"""
        config = self.load_hidden_config()
        team_members = config.get("team_members", {})
        
        report = "🔐 **تقرير الوصول الآمن - فريق EDX**\n"
        report += f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += f"🛡️ حالة الأمان: نشط\n"
        report += f"📊 عدد الأعضاء المخولين: {len(team_members)}\n\n"
        
        for member, data in team_members.items():
            security_level = data.get("security_level", 0)
            role = data.get("role", "غير محدد")
            report += f"✅ {member} - {role} (المستوى: {security_level})\n"
        
        return report

# إنشاء مثيل المحمل الخفي
edx_hidden_loader = EDXHiddenLoader()

# تهيئة النظام عند الاستيراد
if __name__ != "__main__":
    edx_hidden_loader.initialize_hidden_system()
