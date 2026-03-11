# ===================================================================
# ملف إعدادات البوت الموحد والمبسط - جميع المعلومات الحساسة هنا فقط
# ===================================================================

# معلومات المالك الموحد (مالك البوت والغرفة وصاحب الإكراميات)
OWNER_INFO = {
    "username": "duck_05",  # اسم المالك
    "id": "",  # معرف المالك في Highrise
    "display_name": ""  # الاسم المعروض
}

# معلومات البوت الأساسية
BOT_INFO = {
    "token":
    "42f0f927bf9842e98ba3356e5f145585e5097d89e37cb550b6f3dd507e847f5b",  # توكن البوت
    "id": "694f55515452a228fae903da"  # معرف البوت
}

# معلومات الغرفة
ROOM_INFO = {
    "id": "69a876b7cc006889afe7754e"  # معرف الغرفة
}

# إعدادات الأمان
SECURITY_SETTINGS = {
    "auto_detect_moderators": True,  # الكشف التلقائي للمشرفين
    "sync_with_highrise": True,  # المزامنة مع إعدادات Highrise
    "protect_owner_privileges": True,  # حماية صلاحيات المالك
    "allow_privilege_override": False  # السماح بتجاوز الصلاحيات
}

# ===================================================================
# الدوال المساعدة للوصول السريع للبيانات
# ===================================================================


def get_bot_owner_username():
    """إرجاع اسم مالك البوت"""
    return OWNER_INFO["username"]


def get_bot_owner_id():
    """إرجاع معرف مالك البوت"""
    return OWNER_INFO["id"]


def get_room_owner_username():
    """إرجاع اسم مالك الغرفة (نفس مالك البوت)"""
    return OWNER_INFO["username"]


def get_room_owner_id():
    """إرجاع معرف مالك الغرفة (نفس مالك البوت)"""
    return OWNER_INFO["id"]


def get_tip_owner():
    """إرجاع اسم صاحب الإكراميات (نفس مالك البوت)"""
    return OWNER_INFO["username"]


def get_tip_owner_id():
    """إرجاع معرف صاحب الإكراميات (نفس مالك البوت)"""
    return OWNER_INFO["id"]


def get_bot_token():
    """إرجاع توكن البوت"""
    return BOT_INFO["token"]


def get_bot_id():
    """إرجاع معرف البوت"""
    return BOT_INFO["id"]


def get_room_id():
    """إرجاع معرف الغرفة"""
    return ROOM_INFO["id"]


def get_room_primary_owner():
    """إرجاع المالك الأساسي للغرفة (نفس مالك البوت)"""
    return OWNER_INFO["username"]


def get_known_room_owners():
    """إرجاع قائمة المالكين المعروفين للغرفة"""
    return [OWNER_INFO["username"]]


def is_owner_username(username: str) -> bool:
    """التحقق من كون المستخدم هو المالك بالاسم"""
    return username == OWNER_INFO["username"]


def is_owner_id(user_id: str) -> bool:
    """التحقق من كون المستخدم هو المالك بالمعرف"""
    return user_id == OWNER_INFO["id"]


def is_bot_id(user_id: str) -> bool:
    """التحقق من كون المعرف هو البوت نفسه"""
    return user_id == BOT_INFO["id"]


def get_default_moderators():
    """إرجاع قائمة المشرفين الافتراضية (المطور الأساسي فقط)"""
    return [OWNER_INFO["username"]]


# ===================================================================
# دالة التحقق من صحة الإعدادات
# ===================================================================


def validate_config():
    """التحقق من صحة جميع الإعدادات"""
    errors = []

    # فحص معرف المالك
    if not OWNER_INFO["id"] or len(OWNER_INFO["id"]) < 20:
        errors.append("❌ معرف المالك غير صحيح")

    # فحص اسم المالك
    if not OWNER_INFO["username"] or OWNER_INFO["username"].strip() == "":
        errors.append("❌ اسم المالك مطلوب")

    # فحص توكن البوت
    if not BOT_INFO["token"] or len(BOT_INFO["token"]) < 30:
        errors.append("❌ توكن البوت غير صحيح")

    # فحص معرف البوت
    if not BOT_INFO["id"] or len(BOT_INFO["id"]) < 20:
        errors.append("❌ معرف البوت غير صحيح")

    # فحص معرف الغرفة
    if not ROOM_INFO["id"] or len(ROOM_INFO["id"]) < 20:
        errors.append("❌ معرف الغرفة غير صحيح")

    if errors:
        return False, errors
    else:
        return True, ["✅ جميع الإعدادات صحيحة"]


# ===================================================================
# دالة عرض ملخص الإعدادات (آمنة - بدون كشف المعلومات الحساسة)
# ===================================================================


def print_config_summary():
    """طباعة ملخص آمن للإعدادات"""
    print("🔧 ملخص إعدادات البوت المبسط:")
    print("=" * 50)
    print(f"👑 المالك الموحد: {OWNER_INFO['username']}")
    print(f"🆔 معرف المالك: {OWNER_INFO['id'][:10]}...")
    print(f"🤖 معرف البوت: {BOT_INFO['id'][:10]}...")
    print(f"🔑 توكن البوت: {BOT_INFO['token'][:15]}...")
    print(f"🏠 معرف الغرفة: {ROOM_INFO['id'][:10]}...")
    print(f"📋 المشرفين: سيتم تحميلهم من ملف المشرفين")
    print("=" * 50)

    # التحقق من صحة الإعدادات
    is_valid, messages = validate_config()
    for message in messages:
        print(f"   {message}")
    print("=" * 50)


# ===================================================================
# متغيرات للتوافق مع الأكواد القديمة
# ===================================================================

# للتوافق مع الأكواد القديمة
BOT_OWNER = OWNER_INFO  # للتوافق
BOT_OWNER_ID = OWNER_INFO["id"]  # للتوافق
BOT_ID = BOT_INFO["id"]  # للتوافق
ROOM_ID = ROOM_INFO["id"]  # للتوافق
ROOM_OWNER = OWNER_INFO  # للتوافق
TIP_OWNER = OWNER_INFO  # للتوافق

# ===================================================================
# تشغيل الفحص عند استيراد الملف
# ===================================================================

if __name__ == "__main__":
    print("📋 فحص ملف الإعدادات المبسط...")
    print_config_summary()
