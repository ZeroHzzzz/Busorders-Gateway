base_api = "https://api.pinbayun.com"
login_url = base_api + "/api/v4/staff/auths/login/"

bus_info_url = base_api + "/api/v2/staff/shuttlebus/"
bus_time_url = base_api + "/api/v2/staff/shuttlebus/{id}/bustimes/"
bus_date_url = base_api + "/api/v2/staff/shuttlebus/{id}/dates/"
bus_booking_url = base_api + "/api/v3/staff/busorders/"
bus_records_url = base_api + "/api/v1/staff/busorders/"
bus_cancel_url = base_api + "/api/v3/staff/busorders/{id}/cancel/"
bus_bulktask_url = base_api + "/api/v4/staff/busorderbulktask/"

user_qrcode_url = base_api + "/api/v3/pos/staff_qrcode/"
user_company_url = base_api + "/api/v4/staff/auths/get_company/"