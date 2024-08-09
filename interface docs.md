---
title: 校车gateway
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.23"

---

# 校车gateway

Base URLs:

# Authentication

# Default

## POST 手机密码登录

POST /api/login/phone

> Body 请求参数

```json
{
  "phone": "string",
  "password": "string"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» phone|body|string| 是 |none|
|» password|body|string| 是 |none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "data": {
    "age": null,
    "app_model": [
      {
        "ctime": "string",
        "default_load": true,
        "ico": "string",
        "id": 0,
        "is_active": true,
        "is_allow": true,
        "is_customfield": true,
        "is_del": "string",
        "is_menu": true,
        "keyword": "string",
        "mtime": "string",
        "name": "string",
        "order_sort": 0,
        "parent_id": 0,
        "resource": null,
        "type": 0
      }
    ],
    "avatar": null,
    "belong_company": null,
    "bus_favourite_vos": [
      {
        "ctime": "string",
        "id": "string",
        "mtime": "string",
        "shuttle_bus": "string",
        "staff": "string"
      }
    ],
    "bus_monthly_ticket_order_vos": [
      "string"
    ],
    "card_format": 0,
    "card_number": "string",
    "class_id": null,
    "class_name": null,
    "company": "string",
    "company_vo": {
      "addr": "string",
      "agent": null,
      "bus_device_type": 0,
      "card_number_type": 0,
      "company_code": "string",
      "company_name": "string",
      "company_num": "string",
      "company_prefixed": "string",
      "contact_name": "string",
      "contact_phone": "string",
      "ctime": "string",
      "dorm_room_lock_type": 0,
      "expiration_date": null,
      "expired": true,
      "id": "string",
      "img": "string",
      "is_active": true,
      "location": "string",
      "mtime": "string",
      "need_device_binding": true,
      "parent": null,
      "pay_type": 0,
      "province": "string",
      "repair_audit_price": true,
      "serial_number": null,
      "sms_amount": 0,
      "sms_charge_type": 0,
      "source_type": 0,
      "staff_select_building": true
    },
    "contracting_company": null,
    "cost_center": null,
    "ctime": "string",
    "customer_code": "string",
    "department": "string",
    "department_vo": {
      "company": "string",
      "company_vo": {
        "addr": "string",
        "agent": null,
        "bus_device_type": 0,
        "card_number_type": 0,
        "company_code": "string",
        "company_name": "string",
        "company_num": "string",
        "company_prefixed": "string",
        "contact_name": "string",
        "contact_phone": "string",
        "ctime": "string",
        "dorm_room_lock_type": 0,
        "expiration_date": null,
        "expired": true,
        "id": "string",
        "img": "string",
        "is_active": true,
        "location": "string",
        "mtime": "string",
        "need_device_binding": true,
        "parent": null,
        "pay_type": 0,
        "province": "string",
        "repair_audit_price": true,
        "serial_number": null,
        "sms_amount": 0,
        "sms_charge_type": 0,
        "source_type": 0,
        "staff_select_building": true
      },
      "ctime": "string",
      "deep_level": 0,
      "department_code": null,
      "department_name": "string",
      "department_tree": "string",
      "id": "string",
      "mtime": "string",
      "name_path": "string",
      "node_id": 0,
      "parent": null,
      "serial_number": null
    },
    "device_udid": "string",
    "dormitory2_remark": null,
    "due_date": null,
    "education": null,
    "education_obj": null,
    "effective_date": null,
    "email": null,
    "emergency_contact": null,
    "emergency_phone": null,
    "face_img": null,
    "functional_range": null,
    "grade_id": null,
    "grade_name": null,
    "id": "string",
    "id_card": null,
    "induction_date": null,
    "is_active": true,
    "is_busdriver": true,
    "is_off3driver": true,
    "is_patrolman": true,
    "is_repairman": true,
    "job_grade": null,
    "job_number": "string",
    "level": 0,
    "mtime": "string",
    "native_place": null,
    "need_device_binding": true,
    "patrol_man": true,
    "permit_end_date": null,
    "permit_start_date": null,
    "personnel_type": null,
    "phone": "string",
    "position": "string",
    "position_level": "string",
    "profit_center": null,
    "push_clientid": null,
    "real_name": "string",
    "residence_permit_status": 0,
    "resignation_date": null,
    "room": null,
    "sex": 0,
    "staff_type": 0,
    "status": 0,
    "superior": null,
    "token": "string",
    "vehicle_vos": null,
    "vistor_company": null,
    "work_type": null,
    "work_type_name": null,
    "work_type_obj": null,
    "working_place": null
  },
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» data|object|true|none||none|
|»» age|null|true|none||none|
|»» app_model|[object]|true|none||none|
|»»» ctime|string|true|none||none|
|»»» default_load|boolean|true|none||none|
|»»» ico|string|true|none||none|
|»»» id|integer|true|none||none|
|»»» is_active|boolean|true|none||none|
|»»» is_allow|boolean|true|none||none|
|»»» is_customfield|boolean|true|none||none|
|»»» is_del|string|true|none||none|
|»»» is_menu|boolean|true|none||none|
|»»» keyword|string|true|none||none|
|»»» mtime|string|true|none||none|
|»»» name|string|true|none||none|
|»»» order_sort|integer|true|none||none|
|»»» parent_id|integer¦null|true|none||none|
|»»» resource|null|true|none||none|
|»»» type|integer|true|none||none|
|»» avatar|null|true|none||none|
|»» belong_company|null|true|none||none|
|»» bus_favourite_vos|[object]|true|none||none|
|»»» ctime|string|false|none||none|
|»»» id|string|false|none||none|
|»»» mtime|string|false|none||none|
|»»» shuttle_bus|string|false|none||none|
|»»» staff|string|false|none||none|
|»» bus_monthly_ticket_order_vos|[string]|true|none||none|
|»» card_format|integer|true|none||none|
|»» card_number|string|true|none||none|
|»» class_id|null|true|none||none|
|»» class_name|null|true|none||none|
|»» company|string|true|none||none|
|»» company_vo|object|true|none||none|
|»»» addr|string|true|none||none|
|»»» agent|null|true|none||none|
|»»» bus_device_type|integer|true|none||none|
|»»» card_number_type|integer|true|none||none|
|»»» company_code|string|true|none||none|
|»»» company_name|string|true|none||none|
|»»» company_num|string|true|none||none|
|»»» company_prefixed|string|true|none||none|
|»»» contact_name|string|true|none||none|
|»»» contact_phone|string|true|none||none|
|»»» ctime|string|true|none||none|
|»»» dorm_room_lock_type|integer|true|none||none|
|»»» expiration_date|null|true|none||none|
|»»» expired|boolean|true|none||none|
|»»» id|string|true|none||none|
|»»» img|string|true|none||none|
|»»» is_active|boolean|true|none||none|
|»»» location|string|true|none||none|
|»»» mtime|string|true|none||none|
|»»» need_device_binding|boolean|true|none||none|
|»»» parent|null|true|none||none|
|»»» pay_type|integer|true|none||none|
|»»» province|string|true|none||none|
|»»» repair_audit_price|boolean|true|none||none|
|»»» serial_number|null|true|none||none|
|»»» sms_amount|integer|true|none||none|
|»»» sms_charge_type|integer|true|none||none|
|»»» source_type|integer|true|none||none|
|»»» staff_select_building|boolean|true|none||none|
|»» contracting_company|null|true|none||none|
|»» cost_center|null|true|none||none|
|»» ctime|string|true|none||none|
|»» customer_code|string|true|none||none|
|»» department|string|true|none||none|
|»» department_vo|object|true|none||none|
|»»» company|string|true|none||none|
|»»» company_vo|object|true|none||none|
|»»»» addr|string|true|none||none|
|»»»» agent|null|true|none||none|
|»»»» bus_device_type|integer|true|none||none|
|»»»» card_number_type|integer|true|none||none|
|»»»» company_code|string|true|none||none|
|»»»» company_name|string|true|none||none|
|»»»» company_num|string|true|none||none|
|»»»» company_prefixed|string|true|none||none|
|»»»» contact_name|string|true|none||none|
|»»»» contact_phone|string|true|none||none|
|»»»» ctime|string|true|none||none|
|»»»» dorm_room_lock_type|integer|true|none||none|
|»»»» expiration_date|null|true|none||none|
|»»»» expired|boolean|true|none||none|
|»»»» id|string|true|none||none|
|»»»» img|string|true|none||none|
|»»»» is_active|boolean|true|none||none|
|»»»» location|string|true|none||none|
|»»»» mtime|string|true|none||none|
|»»»» need_device_binding|boolean|true|none||none|
|»»»» parent|null|true|none||none|
|»»»» pay_type|integer|true|none||none|
|»»»» province|string|true|none||none|
|»»»» repair_audit_price|boolean|true|none||none|
|»»»» serial_number|null|true|none||none|
|»»»» sms_amount|integer|true|none||none|
|»»»» sms_charge_type|integer|true|none||none|
|»»»» source_type|integer|true|none||none|
|»»»» staff_select_building|boolean|true|none||none|
|»»» ctime|string|true|none||none|
|»»» deep_level|integer|true|none||none|
|»»» department_code|null|true|none||none|
|»»» department_name|string|true|none||none|
|»»» department_tree|string|true|none||none|
|»»» id|string|true|none||none|
|»»» mtime|string|true|none||none|
|»»» name_path|string|true|none||none|
|»»» node_id|integer|true|none||none|
|»»» parent|null|true|none||none|
|»»» serial_number|null|true|none||none|
|»» device_udid|string|true|none||none|
|»» dormitory2_remark|null|true|none||none|
|»» due_date|null|true|none||none|
|»» education|null|true|none||none|
|»» education_obj|null|true|none||none|
|»» effective_date|null|true|none||none|
|»» email|null|true|none||none|
|»» emergency_contact|null|true|none||none|
|»» emergency_phone|null|true|none||none|
|»» face_img|null|true|none||none|
|»» functional_range|null|true|none||none|
|»» grade_id|null|true|none||none|
|»» grade_name|null|true|none||none|
|»» id|string|true|none||none|
|»» id_card|null|true|none||none|
|»» induction_date|null|true|none||none|
|»» is_active|boolean|true|none||none|
|»» is_busdriver|boolean|true|none||none|
|»» is_off3driver|boolean|true|none||none|
|»» is_patrolman|boolean|true|none||none|
|»» is_repairman|boolean|true|none||none|
|»» job_grade|null|true|none||none|
|»» job_number|string|true|none||none|
|»» level|integer|true|none||none|
|»» mtime|string|true|none||none|
|»» native_place|null|true|none||none|
|»» need_device_binding|boolean|true|none||none|
|»» patrol_man|boolean|true|none||none|
|»» permit_end_date|null|true|none||none|
|»» permit_start_date|null|true|none||none|
|»» personnel_type|null|true|none||none|
|»» phone|string|true|none||none|
|»» position|string|true|none||none|
|»» position_level|string|true|none||none|
|»» profit_center|null|true|none||none|
|»» push_clientid|null|true|none||none|
|»» real_name|string|true|none||none|
|»» residence_permit_status|integer|true|none||none|
|»» resignation_date|null|true|none||none|
|»» room|null|true|none||none|
|»» sex|integer|true|none||none|
|»» staff_type|integer|true|none||none|
|»» status|integer|true|none||none|
|»» superior|null|true|none||none|
|»» token|string|true|none||none|
|»» vehicle_vos|null|true|none||none|
|»» vistor_company|null|true|none||none|
|»» work_type|null|true|none||none|
|»» work_type_name|null|true|none||none|
|»» work_type_obj|null|true|none||none|
|»» working_place|null|true|none||none|
|» message|string|true|none||none|

## GET 测试接口

GET /api/test

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "message": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|number|true|none||none|
|» message|string|true|none||none|
|» data|object|true|none||none|

## POST 微信登录

POST /api/login/wx

> Body 请求参数

```json
{
  "corpcode": "string",
  "openid": "string"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» corpcode|body|string| 是 |none|
|» openid|body|string| 是 |none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "message": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|number|true|none||none|
|» message|string|true|none||none|
|» data|object|true|none||none|

# bus

## GET 查询线路信息

GET /api/bus/info

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|page|query|integer| 否 |none|
|page_size|query|integer| 否 |none|
|search|query|string| 否 |none|
|Authorization|header|string| 否 |none|

> 返回示例

> 成功

```json
{
  "code": 200,
  "data": [
    {
      "apply_dispatch_minutes": 0,
      "apply_expired_minutes": 16,
      "auto_dispatch": false,
      "bluk_order": false,
      "bluk_order_staff_levels": "[]",
      "bus_reminder": 30,
      "busfavourite": false,
      "check_mode": 20,
      "check_mode_name": "硬件检票",
      "ctime": "2020-11-06 18:02:35",
      "departure_time": "00:00",
      "driver_dispatch": false,
      "go_stations_json": [
        {
          "id": "981988c0-f847-4196-9a76-12b77d68e493",
          "latitude": 30.298986,
          "longitude": 120.174114,
          "station_name": "邵科馆",
          "station_seq": 0
        },
        {
          "id": "abb1a1e6-c816-451a-9918-cc4c2a766862",
          "latitude": 30.301713,
          "longitude": 120.165992,
          "station_name": "德胜新村公交站",
          "station_seq": 1
        },
        {
          "id": "e6a5069a-8223-4435-85d3-7ebf8a589701",
          "latitude": 30.314427,
          "longitude": 120.154307,
          "station_name": "大关北公交站",
          "station_seq": 2
        },
        {
          "id": "49574235-2fc0-44e3-9b4b-70861804e1d3",
          "latitude": 30.558722,
          "longitude": 120.036983,
          "station_name": "莫干山校区",
          "station_seq": 3
        }
      ],
      "id": "aa93af5b-cc58-4c13-814f-254caefe8d49",
      "instance_days": 10,
      "is_active": true,
      "is_bluk_order_staff_level": false,
      "long_distance": false,
      "mtime": "2024-08-09 14:05:54",
      "net_mode": 0,
      "order_limit_minute": 120,
      "order_limit_on": true,
      "order_mode": 10,
      "order_mode_name": "预约模式",
      "other_price": {
        "student": 0,
        "student_ticket": 0,
        "teacher": 0
      },
      "overtime": false,
      "people_vehicle": false,
      "price": 0,
      "refund_at_dispath": false,
      "refund_at_dispath_limit_minute": 0,
      "remainder_remind": 0,
      "remind_admin": "[]",
      "reserved_seat": 0,
      "return_stations_json": [],
      "seats": 47,
      "shuttle_name": "7号线（朝晖-莫干山）",
      "sort_number": 9,
      "station_names": "",
      "stations_json": [],
      "ticket_check_minutes": 16,
      "ticket_of_buses": true
    },
    {
      "apply_dispatch_minutes": 0,
      "apply_expired_minutes": 16,
      "auto_dispatch": false,
      "bluk_order": false,
      "bluk_order_staff_levels": "[]",
      "bus_reminder": 30,
      "busfavourite": false,
      "check_mode": 20,
      "check_mode_name": "硬件检票",
      "ctime": "2020-11-06 18:02:35",
      "departure_time": "00:00",
      "driver_dispatch": false,
      "go_stations_json": [
        {
          "id": "d3fe4faa-268c-4488-9b72-2beb7746fd7c",
          "latitude": 30.558847,
          "longitude": 120.036948,
          "station_name": "莫干山校区",
          "station_seq": 0
        },
        {
          "id": "da354682-c24c-499a-8bd6-7a0a0e035878",
          "latitude": 30.314548,
          "longitude": 120.154015,
          "station_name": "大关北公交站",
          "station_seq": 1
        },
        {
          "id": "7d9dfdae-45a2-4e43-ae2f-d44d3baac850",
          "latitude": 30.302529,
          "longitude": 120.164839,
          "station_name": "德胜新村公交站",
          "station_seq": 2
        },
        {
          "id": "7c22631a-2b29-47a9-97d8-ccfcc0ba13b1",
          "latitude": 30.298982,
          "longitude": 120.174065,
          "station_name": "邵科馆",
          "station_seq": 3
        }
      ],
      "id": "8860bf68-335e-4ef2-8c9d-61e71beb6d8a",
      "instance_days": 10,
      "is_active": true,
      "is_bluk_order_staff_level": false,
      "long_distance": false,
      "mtime": "2024-08-09 14:05:17",
      "net_mode": 0,
      "order_limit_minute": 120,
      "order_limit_on": true,
      "order_mode": 10,
      "order_mode_name": "预约模式",
      "other_price": {
        "student": 0,
        "student_ticket": 0,
        "teacher": 0
      },
      "overtime": false,
      "people_vehicle": false,
      "price": 0,
      "refund_at_dispath": false,
      "refund_at_dispath_limit_minute": 0,
      "remainder_remind": 0,
      "remind_admin": "[]",
      "reserved_seat": 0,
      "return_stations_json": [],
      "seats": 47,
      "shuttle_name": "7号线（莫干山-朝晖）",
      "sort_number": 10,
      "station_names": "",
      "stations_json": [],
      "ticket_check_minutes": 16,
      "ticket_of_buses": true
    },
    {
      "apply_dispatch_minutes": 0,
      "apply_expired_minutes": 16,
      "auto_dispatch": false,
      "bluk_order": false,
      "bluk_order_staff_levels": "[]",
      "bus_reminder": 30,
      "busfavourite": false,
      "check_mode": 20,
      "check_mode_name": "硬件检票",
      "ctime": "2020-11-06 18:02:36",
      "departure_time": "00:00",
      "driver_dispatch": false,
      "go_stations_json": [
        {
          "id": "d5bd3c72-cbde-4a3c-8984-e3e8bf900933",
          "latitude": 30.299115,
          "longitude": 120.174083,
          "station_name": "邵科馆",
          "station_seq": 0
        },
        {
          "id": "52605c80-629b-45b8-9316-acc1bc04b988",
          "latitude": 30.302708,
          "longitude": 120.175853,
          "station_name": "绍兴路德胜路口公交站",
          "station_seq": 1
        },
        {
          "id": "36b45279-f831-4fe1-a4b2-fa0be2d96e7d",
          "latitude": 30.558871,
          "longitude": 120.036957,
          "station_name": "莫干山校区",
          "station_seq": 2
        }
      ],
      "id": "fecfb912-9522-4438-b760-e50c032d5670",
      "instance_days": 10,
      "is_active": true,
      "is_bluk_order_staff_level": false,
      "long_distance": false,
      "mtime": "2024-07-01 18:59:39",
      "net_mode": 0,
      "order_limit_minute": 120,
      "order_limit_on": true,
      "order_mode": 10,
      "order_mode_name": "预约模式",
      "other_price": {
        "student": 0,
        "student_ticket": 0,
        "teacher": 0
      },
      "overtime": false,
      "people_vehicle": false,
      "price": 0,
      "refund_at_dispath": false,
      "refund_at_dispath_limit_minute": 0,
      "remainder_remind": 0,
      "remind_admin": "[]",
      "reserved_seat": 0,
      "return_stations_json": [],
      "seats": 47,
      "shuttle_name": "8号线（朝晖-莫干山）",
      "sort_number": 11,
      "station_names": "",
      "stations_json": [],
      "ticket_check_minutes": 16,
      "ticket_of_buses": true
    },
    {
      "apply_dispatch_minutes": 0,
      "apply_expired_minutes": 16,
      "auto_dispatch": false,
      "bluk_order": false,
      "bluk_order_staff_levels": "[]",
      "bus_reminder": 30,
      "busfavourite": false,
      "check_mode": 20,
      "check_mode_name": "硬件检票",
      "ctime": "2020-11-06 18:02:36",
      "departure_time": "00:00",
      "driver_dispatch": false,
      "go_stations_json": [
        {
          "id": "45521dd4-1e19-4f1b-9f81-d19dc9bb2b81",
          "latitude": 30.55999,
          "longitude": 120.044941,
          "station_name": "莫干山校区",
          "station_seq": 0
        },
        {
          "id": "b70c075d-eacb-4d15-ba8c-10646c255002",
          "latitude": 30.302732,
          "longitude": 120.175583,
          "station_name": "绍兴路德胜路口公交站",
          "station_seq": 1
        },
        {
          "id": "8d3f8520-4f2f-4626-93fd-dcab4b206b38",
          "latitude": 30.29899,
          "longitude": 120.17411,
          "station_name": "邵科馆",
          "station_seq": 2
        }
      ],
      "id": "a50a7742-898f-4438-8b83-9042d32f6359",
      "instance_days": 10,
      "is_active": true,
      "is_bluk_order_staff_level": false,
      "long_distance": false,
      "mtime": "2024-07-01 13:39:20",
      "net_mode": 0,
      "order_limit_minute": 120,
      "order_limit_on": true,
      "order_mode": 10,
      "order_mode_name": "预约模式",
      "other_price": {
        "student": 0,
        "student_ticket": 0,
        "teacher": 0
      },
      "overtime": false,
      "people_vehicle": false,
      "price": 0,
      "refund_at_dispath": false,
      "refund_at_dispath_limit_minute": 0,
      "remainder_remind": 0,
      "remind_admin": "[]",
      "reserved_seat": 0,
      "return_stations_json": [],
      "seats": 47,
      "shuttle_name": "8号线（莫干山-朝晖）",
      "sort_number": 12,
      "station_names": "",
      "stations_json": [],
      "ticket_check_minutes": 16,
      "ticket_of_buses": true
    },
    {
      "apply_dispatch_minutes": 0,
      "apply_expired_minutes": 16,
      "auto_dispatch": false,
      "bluk_order": false,
      "bluk_order_staff_levels": "[]",
      "bus_reminder": 30,
      "busfavourite": false,
      "check_mode": 20,
      "check_mode_name": "硬件检票",
      "ctime": "2022-10-20 20:24:13",
      "departure_time": "00:00",
      "driver_dispatch": false,
      "go_stations_json": [
        {
          "id": "c41fd935-60b9-447c-8785-a72792dbfd7d",
          "latitude": 30.230081,
          "longitude": 120.044021,
          "station_name": "语林楼",
          "station_seq": 0
        },
        {
          "id": "b5ec8f9e-dd62-49f4-9696-bbb50fcbf65e",
          "latitude": 30.231344,
          "longitude": 120.049095,
          "station_name": "水口公交站",
          "station_seq": 1
        },
        {
          "id": "038d516f-801d-4af9-a73d-9db87a0a38f7",
          "latitude": 30.236707,
          "longitude": 120.056521,
          "station_name": "西溪医院横街公交站",
          "station_seq": 2
        },
        {
          "id": "ce8be150-badb-4080-8a97-4eae48929c85",
          "latitude": 30.250236,
          "longitude": 120.059713,
          "station_name": "留下北公交站",
          "station_seq": 3
        },
        {
          "id": "fdaa9ef7-eeab-4f03-8487-4a9e7d2fb7d3",
          "latitude": 30.278407,
          "longitude": 120.107922,
          "station_name": "古墩路金月巷公交站",
          "station_seq": 4
        },
        {
          "id": "c6befb25-e219-4923-9cd4-0d74e6a7016a",
          "latitude": 30.296199,
          "longitude": 120.104576,
          "station_name": "政新花园公交站",
          "station_seq": 5
        },
        {
          "id": "bb4300cd-5df5-43f8-82de-cd13981f2f16",
          "latitude": 30.304793,
          "longitude": 120.104755,
          "station_name": "三坝公交站",
          "station_seq": 6
        },
        {
          "id": "c57cd970-463b-4ad0-9659-008de066612a",
          "latitude": 30.320424,
          "longitude": 120.101818,
          "station_name": "华东陶瓷建材市场公交站",
          "station_seq": 7
        },
        {
          "id": "46b5065d-e767-4546-93ec-a778b867e1b7",
          "latitude": 30.558703,
          "longitude": 120.037207,
          "station_name": "莫干山校区",
          "station_seq": 8
        }
      ],
      "id": "137543a9-107e-466f-8c3d-fe23c7ca0d02",
      "instance_days": 10,
      "is_active": true,
      "is_bluk_order_staff_level": false,
      "long_distance": false,
      "mtime": "2024-07-19 17:14:19",
      "net_mode": 0,
      "order_limit_minute": 120,
      "order_limit_on": true,
      "order_mode": 10,
      "order_mode_name": "预约模式",
      "other_price": {
        "student": 0,
        "student_ticket": 0,
        "teacher": 0
      },
      "overtime": false,
      "people_vehicle": false,
      "price": 0,
      "refund_at_dispath": false,
      "refund_at_dispath_limit_minute": 0,
      "remainder_remind": 0,
      "remind_admin": "[]",
      "reserved_seat": 0,
      "return_stations_json": [],
      "seats": 0,
      "shuttle_name": "9号线（屏峰-莫干山）",
      "sort_number": 13,
      "station_names": "",
      "stations_json": [],
      "ticket_check_minutes": 16,
      "ticket_of_buses": true
    },
    {
      "apply_dispatch_minutes": 0,
      "apply_expired_minutes": 16,
      "auto_dispatch": false,
      "bluk_order": false,
      "bluk_order_staff_levels": "[]",
      "bus_reminder": 30,
      "busfavourite": false,
      "check_mode": 20,
      "check_mode_name": "硬件检票",
      "ctime": "2022-10-20 20:40:49",
      "departure_time": "00:00",
      "driver_dispatch": false,
      "go_stations_json": [
        {
          "id": "dde5e5e2-5eff-458b-ac15-84d117df7261",
          "latitude": 30.557927,
          "longitude": 120.036576,
          "station_name": "莫干山校区",
          "station_seq": 0
        },
        {
          "id": "b59d8ac2-437f-4617-8660-567ab4dd0009",
          "latitude": 30.31834,
          "longitude": 120.102251,
          "station_name": "华东陶瓷建材市场公交站",
          "station_seq": 1
        },
        {
          "id": "c0a451f2-1f5d-494b-a1c6-d2a80afebddb",
          "latitude": 30.305117,
          "longitude": 120.104439,
          "station_name": "三坝公交站",
          "station_seq": 2
        },
        {
          "id": "23d4a7ce-63c5-4de2-9313-0611d4e1a5c4",
          "latitude": 30.296188,
          "longitude": 120.104578,
          "station_name": "政新花园公交站",
          "station_seq": 3
        },
        {
          "id": "3877bdcc-7e73-4ab1-a35b-283a33790357",
          "latitude": 30.279816,
          "longitude": 120.10765,
          "station_name": "古墩路金月巷公交站",
          "station_seq": 4
        },
        {
          "id": "fab5f24e-f826-4e48-83ed-5537c10ea0bb",
          "latitude": 30.250428,
          "longitude": 120.059268,
          "station_name": "留下北公交站",
          "station_seq": 5
        },
        {
          "id": "ad257597-c56b-4451-b89c-869a6ad5a7c5",
          "latitude": 30.236814,
          "longitude": 120.056285,
          "station_name": "西溪医院横街公交站",
          "station_seq": 6
        },
        {
          "id": "ca6dd877-fe78-4e0f-804f-470604df1d2a",
          "latitude": 30.238027,
          "longitude": 120.051897,
          "station_name": "1A区块/3号楼西侧",
          "station_seq": 7
        },
        {
          "id": "9b578c3d-8680-4595-9d03-6f840f8b4591",
          "latitude": 30.235733,
          "longitude": 120.047383,
          "station_name": "乌溪江路北口",
          "station_seq": 8
        },
        {
          "id": "d9cc56a0-1a5b-4d4a-a85e-f9cb3be28fc0",
          "latitude": 30.229598,
          "longitude": 120.039603,
          "station_name": "古运河路西口（图书馆西南侧）",
          "station_seq": 9
        },
        {
          "id": "fb42bfb1-4a0b-4bd6-9b27-17cee83230f5",
          "latitude": 30.230062,
          "longitude": 120.044001,
          "station_name": "语林楼",
          "station_seq": 10
        }
      ],
      "id": "a899298d-12ac-4fd6-b872-af1a5e11a714",
      "instance_days": 10,
      "is_active": true,
      "is_bluk_order_staff_level": false,
      "long_distance": false,
      "mtime": "2024-07-19 17:18:34",
      "net_mode": 0,
      "order_limit_minute": 120,
      "order_limit_on": true,
      "order_mode": 10,
      "order_mode_name": "预约模式",
      "other_price": {
        "student": 0,
        "student_ticket": 0,
        "teacher": 0
      },
      "overtime": false,
      "people_vehicle": false,
      "price": 0,
      "refund_at_dispath": false,
      "refund_at_dispath_limit_minute": 0,
      "remainder_remind": 0,
      "remind_admin": "[]",
      "reserved_seat": 0,
      "return_stations_json": [],
      "seats": 0,
      "shuttle_name": "9号线（莫干山-屏峰）",
      "sort_number": 14,
      "station_names": "",
      "stations_json": [],
      "ticket_check_minutes": 16,
      "ticket_of_buses": true
    },
    {
      "apply_dispatch_minutes": 0,
      "apply_expired_minutes": 16,
      "auto_dispatch": false,
      "bluk_order": false,
      "bluk_order_staff_levels": "[]",
      "bus_reminder": 30,
      "busfavourite": false,
      "check_mode": 20,
      "check_mode_name": "硬件检票",
      "ctime": "2022-10-20 20:53:04",
      "departure_time": "00:00",
      "driver_dispatch": false,
      "go_stations_json": [
        {
          "id": "3458c258-dc10-4ae0-9e32-4c1c0540361b",
          "latitude": 30.27845,
          "longitude": 120.107915,
          "station_name": "古墩路金月巷公交站",
          "station_seq": 0
        },
        {
          "id": "ecdb99c1-6497-4297-8501-4f4379f9622d",
          "latitude": 30.296226,
          "longitude": 120.104578,
          "station_name": "政新花园公交站",
          "station_seq": 1
        },
        {
          "id": "4265777c-696b-4a29-b8c7-06673a0b048b",
          "latitude": 30.304793,
          "longitude": 120.104767,
          "station_name": "三坝公交站",
          "station_seq": 2
        },
        {
          "id": "134fd35d-cf47-4dd2-b396-44b51dafbfd8",
          "latitude": 30.32042,
          "longitude": 120.101829,
          "station_name": "华东陶瓷建材市场公交站",
          "station_seq": 3
        },
        {
          "id": "bf773965-e14b-43d3-ae7e-36394d20ccce",
          "latitude": 30.330328,
          "longitude": 120.10393,
          "station_name": "水映苑公交站",
          "station_seq": 4
        },
        {
          "id": "5a14d6fb-9b40-4699-9e8e-d87193b21669",
          "latitude": 30.558707,
          "longitude": 120.037201,
          "station_name": "莫干山校区",
          "station_seq": 5
        }
      ],
      "id": "a7b72f92-0793-4bc6-a84f-caf922718e71",
      "instance_days": 10,
      "is_active": true,
      "is_bluk_order_staff_level": false,
      "long_distance": false,
      "mtime": "2023-12-15 16:23:24",
      "net_mode": 0,
      "order_limit_minute": 120,
      "order_limit_on": true,
      "order_mode": 10,
      "order_mode_name": "预约模式",
      "other_price": {
        "student": 0,
        "student_ticket": 0,
        "teacher": 0
      },
      "overtime": false,
      "people_vehicle": false,
      "price": 0,
      "refund_at_dispath": false,
      "refund_at_dispath_limit_minute": 0,
      "remainder_remind": 0,
      "remind_admin": "[]",
      "reserved_seat": 0,
      "return_stations_json": [],
      "seats": 47,
      "shuttle_name": "9号线支线（金月巷-莫干山）",
      "sort_number": 15,
      "station_names": "",
      "stations_json": [],
      "ticket_check_minutes": 16,
      "ticket_of_buses": true
    },
    {
      "apply_dispatch_minutes": 0,
      "apply_expired_minutes": 16,
      "auto_dispatch": false,
      "bluk_order": false,
      "bluk_order_staff_levels": "[]",
      "bus_reminder": 30,
      "busfavourite": false,
      "check_mode": 20,
      "check_mode_name": "硬件检票",
      "ctime": "2022-10-20 20:56:08",
      "departure_time": "00:00",
      "driver_dispatch": false,
      "go_stations_json": [
        {
          "id": "d8b7303d-7468-4f82-bad4-f5f7ecb9298b",
          "latitude": 30.55798,
          "longitude": 120.036644,
          "station_name": "莫干山校区",
          "station_seq": 0
        },
        {
          "id": "2234ff36-e045-49c1-b166-87396b65fedd",
          "latitude": 30.330285,
          "longitude": 120.103741,
          "station_name": "水映苑公交站",
          "station_seq": 1
        },
        {
          "id": "848480c9-d14d-4267-97d8-fde5d9effa5f",
          "latitude": 30.318316,
          "longitude": 120.102229,
          "station_name": "华东陶瓷建材市场公交站",
          "station_seq": 2
        },
        {
          "id": "d00640ed-e195-46c4-a35d-316a158d2847",
          "latitude": 30.305112,
          "longitude": 120.104421,
          "station_name": "三坝公交站",
          "station_seq": 3
        },
        {
          "id": "16b71394-14e9-4ad1-b206-08630f203b29",
          "latitude": 30.29621,
          "longitude": 120.104582,
          "station_name": "政新花园公交站",
          "station_seq": 4
        },
        {
          "id": "be763bca-69dd-4d8c-8c42-d78236773b0e",
          "latitude": 30.279819,
          "longitude": 120.107646,
          "station_name": "古墩路金月巷公交站",
          "station_seq": 5
        }
      ],
      "id": "0668e5b0-7c3d-47b7-a4be-de6995d571eb",
      "instance_days": 10,
      "is_active": true,
      "is_bluk_order_staff_level": false,
      "long_distance": false,
      "mtime": "2023-12-15 16:23:24",
      "net_mode": 0,
      "order_limit_minute": 120,
      "order_limit_on": true,
      "order_mode": 10,
      "order_mode_name": "预约模式",
      "other_price": {
        "student": 0,
        "student_ticket": 0,
        "teacher": 0
      },
      "overtime": false,
      "people_vehicle": false,
      "price": 0,
      "refund_at_dispath": false,
      "refund_at_dispath_limit_minute": 0,
      "remainder_remind": 0,
      "remind_admin": "[]",
      "reserved_seat": 0,
      "return_stations_json": [],
      "seats": 47,
      "shuttle_name": "9号线支线（莫干山-金月巷）",
      "sort_number": 16,
      "station_names": "",
      "stations_json": [],
      "ticket_check_minutes": 16,
      "ticket_of_buses": true
    }
  ],
  "message": "Success"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» data|[object]|true|none||none|
|»» apply_dispatch_minutes|integer|true|none||none|
|»» apply_expired_minutes|integer|true|none||none|
|»» auto_dispatch|boolean|true|none||none|
|»» bluk_order|boolean|true|none||none|
|»» bluk_order_staff_levels|string|true|none||none|
|»» bus_reminder|integer|true|none||none|
|»» busfavourite|boolean|true|none||none|
|»» check_mode|integer|true|none||none|
|»» check_mode_name|string|true|none||none|
|»» ctime|string|true|none||none|
|»» departure_time|string|true|none||none|
|»» driver_dispatch|boolean|true|none||none|
|»» go_stations_json|[object]|true|none||none|
|»»» id|string|true|none||none|
|»»» latitude|number|true|none||none|
|»»» longitude|number|true|none||none|
|»»» station_name|string|true|none||none|
|»»» station_seq|integer|true|none||none|
|»» id|string|true|none||none|
|»» instance_days|integer|true|none||none|
|»» is_active|boolean|true|none||none|
|»» is_bluk_order_staff_level|boolean|true|none||none|
|»» long_distance|boolean|true|none||none|
|»» mtime|string|true|none||none|
|»» net_mode|integer|true|none||none|
|»» order_limit_minute|integer|true|none||none|
|»» order_limit_on|boolean|true|none||none|
|»» order_mode|integer|true|none||none|
|»» order_mode_name|string|true|none||none|
|»» other_price|object|true|none||none|
|»»» student|integer|true|none||none|
|»»» student_ticket|integer|true|none||none|
|»»» teacher|integer|true|none||none|
|»» overtime|boolean|true|none||none|
|»» people_vehicle|boolean|true|none||none|
|»» price|integer|true|none||none|
|»» refund_at_dispath|boolean|true|none||none|
|»» refund_at_dispath_limit_minute|integer|true|none||none|
|»» remainder_remind|integer|true|none||none|
|»» remind_admin|string|true|none||none|
|»» reserved_seat|integer|true|none||none|
|»» return_stations_json|[string]|true|none||none|
|»» seats|integer|true|none||none|
|»» shuttle_name|string|true|none||none|
|»» sort_number|integer|true|none||none|
|»» station_names|string|true|none||none|
|»» stations_json|[string]|true|none||none|
|»» ticket_check_minutes|integer|true|none||none|
|»» ticket_of_buses|boolean|true|none||none|
|» message|string|true|none||none|

## GET 查询线路时间表

GET /api/bus/time

> Body 请求参数

```json
{
  "shuttle_type": 0,
  "id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Authorization|header|string| 否 |none|
|body|body|object| 否 |none|
|» shuttle_type|body|number| 是 |none|
|» id|body|string| 是 |班车线路的id|

> 返回示例

> 成功

```json
{
  "code": 200,
  "data": [
    {
      "ctime": "2022-10-20 21:40:37",
      "departure_time": "08:00",
      "id": "4dba3520-2cb0-4c21-a743-78590ff20f0a",
      "mtime": "2022-10-20 21:40:37",
      "punctuality_time": null,
      "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
      "shuttle_bus_vo": {
        "apply_dispatch_minutes": 0,
        "apply_expired_minutes": 16,
        "auto_dispatch": false,
        "bluk_order": false,
        "bluk_order_staff_levels": "[]",
        "bus_reminder": 30,
        "bus_times": [
          {
            "ctime": "2022-10-20 20:40:49",
            "departure_time": "06:40",
            "id": "1b192003-143c-4221-8148-176517e7e2fe",
            "mtime": "2022-10-20 20:40:49",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2023-01-05 09:57:52",
            "departure_time": "07:20",
            "id": "66a398e6-ce32-4d14-bd05-28002e24ecfd",
            "mtime": "2023-01-05 09:57:52",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:37",
            "departure_time": "08:00",
            "id": "4dba3520-2cb0-4c21-a743-78590ff20f0a",
            "mtime": "2022-10-20 21:40:37",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:37",
            "departure_time": "10:10",
            "id": "a7114208-2153-47ca-981e-04a5ecc70421",
            "mtime": "2022-10-20 21:40:37",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:47:14",
            "departure_time": "12:00",
            "id": "9eb822d3-c41f-43b3-b28e-9fe5e0efbda5",
            "mtime": "2022-10-20 21:47:14",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:37",
            "departure_time": "13:30",
            "id": "06dba5b3-1624-4917-8706-608061465bdf",
            "mtime": "2022-10-20 21:40:37",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-12-25 10:21:34",
            "departure_time": "16:30",
            "id": "8f329917-8c30-4d35-aa14-7e6265634f31",
            "mtime": "2022-12-25 10:21:34",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:47:14",
            "departure_time": "17:00",
            "id": "fa3e330b-1bae-4f50-9ebb-163af03981b9",
            "mtime": "2022-10-20 21:47:14",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:38",
            "departure_time": "17:30",
            "id": "542548a4-f98c-4c38-8bd1-de0c81d465e8",
            "mtime": "2022-10-20 21:40:38",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-12-25 10:21:34",
            "departure_time": "20:30",
            "id": "0bd4a657-bd62-4c21-b5ed-11dd6665abee",
            "mtime": "2022-12-25 10:21:34",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:38",
            "departure_time": "21:30",
            "id": "f2b5cbcd-5657-4924-bf35-1dc208c6efea",
            "mtime": "2022-10-20 21:40:38",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          }
        ],
        "check_mode": 20,
        "check_mode_name": "硬件检票",
        "ctime": "2022-10-20 20:40:49",
        "departure_time": "00:00",
        "driver_dispatch": false,
        "go_stations_json": [
          {
            "id": "dde5e5e2-5eff-458b-ac15-84d117df7261",
            "latitude": 30.557927,
            "longitude": 120.036576,
            "station_name": "莫干山校区",
            "station_seq": 0
          },
          {
            "id": "b59d8ac2-437f-4617-8660-567ab4dd0009",
            "latitude": 30.31834,
            "longitude": 120.102251,
            "station_name": "华东陶瓷建材市场公交站",
            "station_seq": 1
          },
          {
            "id": "c0a451f2-1f5d-494b-a1c6-d2a80afebddb",
            "latitude": 30.305117,
            "longitude": 120.104439,
            "station_name": "三坝公交站",
            "station_seq": 2
          },
          {
            "id": "23d4a7ce-63c5-4de2-9313-0611d4e1a5c4",
            "latitude": 30.296188,
            "longitude": 120.104578,
            "station_name": "政新花园公交站",
            "station_seq": 3
          },
          {
            "id": "3877bdcc-7e73-4ab1-a35b-283a33790357",
            "latitude": 30.279816,
            "longitude": 120.10765,
            "station_name": "古墩路金月巷公交站",
            "station_seq": 4
          },
          {
            "id": "fab5f24e-f826-4e48-83ed-5537c10ea0bb",
            "latitude": 30.250428,
            "longitude": 120.059268,
            "station_name": "留下北公交站",
            "station_seq": 5
          },
          {
            "id": "ad257597-c56b-4451-b89c-869a6ad5a7c5",
            "latitude": 30.236814,
            "longitude": 120.056285,
            "station_name": "西溪医院横街公交站",
            "station_seq": 6
          },
          {
            "id": "ca6dd877-fe78-4e0f-804f-470604df1d2a",
            "latitude": 30.238027,
            "longitude": 120.051897,
            "station_name": "1A区块/3号楼西侧",
            "station_seq": 7
          },
          {
            "id": "9b578c3d-8680-4595-9d03-6f840f8b4591",
            "latitude": 30.235733,
            "longitude": 120.047383,
            "station_name": "乌溪江路北口",
            "station_seq": 8
          },
          {
            "id": "d9cc56a0-1a5b-4d4a-a85e-f9cb3be28fc0",
            "latitude": 30.229598,
            "longitude": 120.039603,
            "station_name": "古运河路西口（图书馆西南侧）",
            "station_seq": 9
          },
          {
            "id": "fb42bfb1-4a0b-4bd6-9b27-17cee83230f5",
            "latitude": 30.230062,
            "longitude": 120.044001,
            "station_name": "语林楼",
            "station_seq": 10
          }
        ],
        "id": "a899298d-12ac-4fd6-b872-af1a5e11a714",
        "instance_days": 10,
        "is_active": true,
        "is_bluk_order_staff_level": false,
        "long_distance": false,
        "mtime": "2024-07-19 17:18:34",
        "net_mode": 0,
        "order_limit_minute": 120,
        "order_limit_on": true,
        "order_mode": 10,
        "order_mode_name": "预约模式",
        "other_price": {
          "student": 0,
          "student_ticket": 0,
          "teacher": 0
        },
        "overtime": false,
        "people_vehicle": false,
        "price": 0,
        "refund_at_dispath": false,
        "refund_at_dispath_limit_minute": 0,
        "remainder_remind": 0,
        "remind_admin": "[]",
        "reserved_seat": 0,
        "return_stations_json": [],
        "seats": 0,
        "shuttle_name": "9号线（莫干山-屏峰）",
        "sort_number": 14,
        "station_names": [],
        "stations_json": [
          {
            "id": "dde5e5e2-5eff-458b-ac15-84d117df7261",
            "latitude": 30.557927,
            "longitude": 120.036576,
            "station_name": "莫干山校区",
            "station_seq": 0
          },
          {
            "id": "b59d8ac2-437f-4617-8660-567ab4dd0009",
            "latitude": 30.31834,
            "longitude": 120.102251,
            "station_name": "华东陶瓷建材市场公交站",
            "station_seq": 1
          },
          {
            "id": "c0a451f2-1f5d-494b-a1c6-d2a80afebddb",
            "latitude": 30.305117,
            "longitude": 120.104439,
            "station_name": "三坝公交站",
            "station_seq": 2
          },
          {
            "id": "23d4a7ce-63c5-4de2-9313-0611d4e1a5c4",
            "latitude": 30.296188,
            "longitude": 120.104578,
            "station_name": "政新花园公交站",
            "station_seq": 3
          },
          {
            "id": "3877bdcc-7e73-4ab1-a35b-283a33790357",
            "latitude": 30.279816,
            "longitude": 120.10765,
            "station_name": "古墩路金月巷公交站",
            "station_seq": 4
          },
          {
            "id": "fab5f24e-f826-4e48-83ed-5537c10ea0bb",
            "latitude": 30.250428,
            "longitude": 120.059268,
            "station_name": "留下北公交站",
            "station_seq": 5
          },
          {
            "id": "ad257597-c56b-4451-b89c-869a6ad5a7c5",
            "latitude": 30.236814,
            "longitude": 120.056285,
            "station_name": "西溪医院横街公交站",
            "station_seq": 6
          },
          {
            "id": "ca6dd877-fe78-4e0f-804f-470604df1d2a",
            "latitude": 30.238027,
            "longitude": 120.051897,
            "station_name": "1A区块/3号楼西侧",
            "station_seq": 7
          },
          {
            "id": "9b578c3d-8680-4595-9d03-6f840f8b4591",
            "latitude": 30.235733,
            "longitude": 120.047383,
            "station_name": "乌溪江路北口",
            "station_seq": 8
          },
          {
            "id": "d9cc56a0-1a5b-4d4a-a85e-f9cb3be28fc0",
            "latitude": 30.229598,
            "longitude": 120.039603,
            "station_name": "古运河路西口（图书馆西南侧）",
            "station_seq": 9
          },
          {
            "id": "fb42bfb1-4a0b-4bd6-9b27-17cee83230f5",
            "latitude": 30.230062,
            "longitude": 120.044001,
            "station_name": "语林楼",
            "station_seq": 10
          }
        ],
        "ticket_check_minutes": 16,
        "ticket_of_buses": true
      },
      "shuttle_type": -10,
      "shuttle_type_name": "去程"
    },
    {
      "ctime": "2022-10-20 21:47:14",
      "departure_time": "12:00",
      "id": "9eb822d3-c41f-43b3-b28e-9fe5e0efbda5",
      "mtime": "2022-10-20 21:47:14",
      "punctuality_time": null,
      "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
      "shuttle_bus_vo": {
        "apply_dispatch_minutes": 0,
        "apply_expired_minutes": 16,
        "auto_dispatch": false,
        "bluk_order": false,
        "bluk_order_staff_levels": "[]",
        "bus_reminder": 30,
        "bus_times": [
          {
            "ctime": "2022-10-20 20:40:49",
            "departure_time": "06:40",
            "id": "1b192003-143c-4221-8148-176517e7e2fe",
            "mtime": "2022-10-20 20:40:49",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2023-01-05 09:57:52",
            "departure_time": "07:20",
            "id": "66a398e6-ce32-4d14-bd05-28002e24ecfd",
            "mtime": "2023-01-05 09:57:52",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:37",
            "departure_time": "08:00",
            "id": "4dba3520-2cb0-4c21-a743-78590ff20f0a",
            "mtime": "2022-10-20 21:40:37",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:37",
            "departure_time": "10:10",
            "id": "a7114208-2153-47ca-981e-04a5ecc70421",
            "mtime": "2022-10-20 21:40:37",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:47:14",
            "departure_time": "12:00",
            "id": "9eb822d3-c41f-43b3-b28e-9fe5e0efbda5",
            "mtime": "2022-10-20 21:47:14",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:37",
            "departure_time": "13:30",
            "id": "06dba5b3-1624-4917-8706-608061465bdf",
            "mtime": "2022-10-20 21:40:37",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-12-25 10:21:34",
            "departure_time": "16:30",
            "id": "8f329917-8c30-4d35-aa14-7e6265634f31",
            "mtime": "2022-12-25 10:21:34",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:47:14",
            "departure_time": "17:00",
            "id": "fa3e330b-1bae-4f50-9ebb-163af03981b9",
            "mtime": "2022-10-20 21:47:14",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:38",
            "departure_time": "17:30",
            "id": "542548a4-f98c-4c38-8bd1-de0c81d465e8",
            "mtime": "2022-10-20 21:40:38",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-12-25 10:21:34",
            "departure_time": "20:30",
            "id": "0bd4a657-bd62-4c21-b5ed-11dd6665abee",
            "mtime": "2022-12-25 10:21:34",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:38",
            "departure_time": "21:30",
            "id": "f2b5cbcd-5657-4924-bf35-1dc208c6efea",
            "mtime": "2022-10-20 21:40:38",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          }
        ],
        "check_mode": 20,
        "check_mode_name": "硬件检票",
        "ctime": "2022-10-20 20:40:49",
        "departure_time": "00:00",
        "driver_dispatch": false,
        "go_stations_json": [
          {
            "id": "dde5e5e2-5eff-458b-ac15-84d117df7261",
            "latitude": 30.557927,
            "longitude": 120.036576,
            "station_name": "莫干山校区",
            "station_seq": 0
          },
          {
            "id": "b59d8ac2-437f-4617-8660-567ab4dd0009",
            "latitude": 30.31834,
            "longitude": 120.102251,
            "station_name": "华东陶瓷建材市场公交站",
            "station_seq": 1
          },
          {
            "id": "c0a451f2-1f5d-494b-a1c6-d2a80afebddb",
            "latitude": 30.305117,
            "longitude": 120.104439,
            "station_name": "三坝公交站",
            "station_seq": 2
          },
          {
            "id": "23d4a7ce-63c5-4de2-9313-0611d4e1a5c4",
            "latitude": 30.296188,
            "longitude": 120.104578,
            "station_name": "政新花园公交站",
            "station_seq": 3
          },
          {
            "id": "3877bdcc-7e73-4ab1-a35b-283a33790357",
            "latitude": 30.279816,
            "longitude": 120.10765,
            "station_name": "古墩路金月巷公交站",
            "station_seq": 4
          },
          {
            "id": "fab5f24e-f826-4e48-83ed-5537c10ea0bb",
            "latitude": 30.250428,
            "longitude": 120.059268,
            "station_name": "留下北公交站",
            "station_seq": 5
          },
          {
            "id": "ad257597-c56b-4451-b89c-869a6ad5a7c5",
            "latitude": 30.236814,
            "longitude": 120.056285,
            "station_name": "西溪医院横街公交站",
            "station_seq": 6
          },
          {
            "id": "ca6dd877-fe78-4e0f-804f-470604df1d2a",
            "latitude": 30.238027,
            "longitude": 120.051897,
            "station_name": "1A区块/3号楼西侧",
            "station_seq": 7
          },
          {
            "id": "9b578c3d-8680-4595-9d03-6f840f8b4591",
            "latitude": 30.235733,
            "longitude": 120.047383,
            "station_name": "乌溪江路北口",
            "station_seq": 8
          },
          {
            "id": "d9cc56a0-1a5b-4d4a-a85e-f9cb3be28fc0",
            "latitude": 30.229598,
            "longitude": 120.039603,
            "station_name": "古运河路西口（图书馆西南侧）",
            "station_seq": 9
          },
          {
            "id": "fb42bfb1-4a0b-4bd6-9b27-17cee83230f5",
            "latitude": 30.230062,
            "longitude": 120.044001,
            "station_name": "语林楼",
            "station_seq": 10
          }
        ],
        "id": "a899298d-12ac-4fd6-b872-af1a5e11a714",
        "instance_days": 10,
        "is_active": true,
        "is_bluk_order_staff_level": false,
        "long_distance": false,
        "mtime": "2024-07-19 17:18:34",
        "net_mode": 0,
        "order_limit_minute": 120,
        "order_limit_on": true,
        "order_mode": 10,
        "order_mode_name": "预约模式",
        "other_price": {
          "student": 0,
          "student_ticket": 0,
          "teacher": 0
        },
        "overtime": false,
        "people_vehicle": false,
        "price": 0,
        "refund_at_dispath": false,
        "refund_at_dispath_limit_minute": 0,
        "remainder_remind": 0,
        "remind_admin": "[]",
        "reserved_seat": 0,
        "return_stations_json": [],
        "seats": 0,
        "shuttle_name": "9号线（莫干山-屏峰）",
        "sort_number": 14,
        "station_names": [],
        "stations_json": [
          {
            "id": "dde5e5e2-5eff-458b-ac15-84d117df7261",
            "latitude": 30.557927,
            "longitude": 120.036576,
            "station_name": "莫干山校区",
            "station_seq": 0
          },
          {
            "id": "b59d8ac2-437f-4617-8660-567ab4dd0009",
            "latitude": 30.31834,
            "longitude": 120.102251,
            "station_name": "华东陶瓷建材市场公交站",
            "station_seq": 1
          },
          {
            "id": "c0a451f2-1f5d-494b-a1c6-d2a80afebddb",
            "latitude": 30.305117,
            "longitude": 120.104439,
            "station_name": "三坝公交站",
            "station_seq": 2
          },
          {
            "id": "23d4a7ce-63c5-4de2-9313-0611d4e1a5c4",
            "latitude": 30.296188,
            "longitude": 120.104578,
            "station_name": "政新花园公交站",
            "station_seq": 3
          },
          {
            "id": "3877bdcc-7e73-4ab1-a35b-283a33790357",
            "latitude": 30.279816,
            "longitude": 120.10765,
            "station_name": "古墩路金月巷公交站",
            "station_seq": 4
          },
          {
            "id": "fab5f24e-f826-4e48-83ed-5537c10ea0bb",
            "latitude": 30.250428,
            "longitude": 120.059268,
            "station_name": "留下北公交站",
            "station_seq": 5
          },
          {
            "id": "ad257597-c56b-4451-b89c-869a6ad5a7c5",
            "latitude": 30.236814,
            "longitude": 120.056285,
            "station_name": "西溪医院横街公交站",
            "station_seq": 6
          },
          {
            "id": "ca6dd877-fe78-4e0f-804f-470604df1d2a",
            "latitude": 30.238027,
            "longitude": 120.051897,
            "station_name": "1A区块/3号楼西侧",
            "station_seq": 7
          },
          {
            "id": "9b578c3d-8680-4595-9d03-6f840f8b4591",
            "latitude": 30.235733,
            "longitude": 120.047383,
            "station_name": "乌溪江路北口",
            "station_seq": 8
          },
          {
            "id": "d9cc56a0-1a5b-4d4a-a85e-f9cb3be28fc0",
            "latitude": 30.229598,
            "longitude": 120.039603,
            "station_name": "古运河路西口（图书馆西南侧）",
            "station_seq": 9
          },
          {
            "id": "fb42bfb1-4a0b-4bd6-9b27-17cee83230f5",
            "latitude": 30.230062,
            "longitude": 120.044001,
            "station_name": "语林楼",
            "station_seq": 10
          }
        ],
        "ticket_check_minutes": 16,
        "ticket_of_buses": true
      },
      "shuttle_type": -10,
      "shuttle_type_name": "去程"
    },
    {
      "ctime": "2022-12-25 10:21:34",
      "departure_time": "16:30",
      "id": "8f329917-8c30-4d35-aa14-7e6265634f31",
      "mtime": "2022-12-25 10:21:34",
      "punctuality_time": null,
      "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
      "shuttle_bus_vo": {
        "apply_dispatch_minutes": 0,
        "apply_expired_minutes": 16,
        "auto_dispatch": false,
        "bluk_order": false,
        "bluk_order_staff_levels": "[]",
        "bus_reminder": 30,
        "bus_times": [
          {
            "ctime": "2022-10-20 20:40:49",
            "departure_time": "06:40",
            "id": "1b192003-143c-4221-8148-176517e7e2fe",
            "mtime": "2022-10-20 20:40:49",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2023-01-05 09:57:52",
            "departure_time": "07:20",
            "id": "66a398e6-ce32-4d14-bd05-28002e24ecfd",
            "mtime": "2023-01-05 09:57:52",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:37",
            "departure_time": "08:00",
            "id": "4dba3520-2cb0-4c21-a743-78590ff20f0a",
            "mtime": "2022-10-20 21:40:37",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:37",
            "departure_time": "10:10",
            "id": "a7114208-2153-47ca-981e-04a5ecc70421",
            "mtime": "2022-10-20 21:40:37",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:47:14",
            "departure_time": "12:00",
            "id": "9eb822d3-c41f-43b3-b28e-9fe5e0efbda5",
            "mtime": "2022-10-20 21:47:14",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:37",
            "departure_time": "13:30",
            "id": "06dba5b3-1624-4917-8706-608061465bdf",
            "mtime": "2022-10-20 21:40:37",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-12-25 10:21:34",
            "departure_time": "16:30",
            "id": "8f329917-8c30-4d35-aa14-7e6265634f31",
            "mtime": "2022-12-25 10:21:34",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:47:14",
            "departure_time": "17:00",
            "id": "fa3e330b-1bae-4f50-9ebb-163af03981b9",
            "mtime": "2022-10-20 21:47:14",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:38",
            "departure_time": "17:30",
            "id": "542548a4-f98c-4c38-8bd1-de0c81d465e8",
            "mtime": "2022-10-20 21:40:38",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-12-25 10:21:34",
            "departure_time": "20:30",
            "id": "0bd4a657-bd62-4c21-b5ed-11dd6665abee",
            "mtime": "2022-12-25 10:21:34",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:38",
            "departure_time": "21:30",
            "id": "f2b5cbcd-5657-4924-bf35-1dc208c6efea",
            "mtime": "2022-10-20 21:40:38",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          }
        ],
        "check_mode": 20,
        "check_mode_name": "硬件检票",
        "ctime": "2022-10-20 20:40:49",
        "departure_time": "00:00",
        "driver_dispatch": false,
        "go_stations_json": [
          {
            "id": "dde5e5e2-5eff-458b-ac15-84d117df7261",
            "latitude": 30.557927,
            "longitude": 120.036576,
            "station_name": "莫干山校区",
            "station_seq": 0
          },
          {
            "id": "b59d8ac2-437f-4617-8660-567ab4dd0009",
            "latitude": 30.31834,
            "longitude": 120.102251,
            "station_name": "华东陶瓷建材市场公交站",
            "station_seq": 1
          },
          {
            "id": "c0a451f2-1f5d-494b-a1c6-d2a80afebddb",
            "latitude": 30.305117,
            "longitude": 120.104439,
            "station_name": "三坝公交站",
            "station_seq": 2
          },
          {
            "id": "23d4a7ce-63c5-4de2-9313-0611d4e1a5c4",
            "latitude": 30.296188,
            "longitude": 120.104578,
            "station_name": "政新花园公交站",
            "station_seq": 3
          },
          {
            "id": "3877bdcc-7e73-4ab1-a35b-283a33790357",
            "latitude": 30.279816,
            "longitude": 120.10765,
            "station_name": "古墩路金月巷公交站",
            "station_seq": 4
          },
          {
            "id": "fab5f24e-f826-4e48-83ed-5537c10ea0bb",
            "latitude": 30.250428,
            "longitude": 120.059268,
            "station_name": "留下北公交站",
            "station_seq": 5
          },
          {
            "id": "ad257597-c56b-4451-b89c-869a6ad5a7c5",
            "latitude": 30.236814,
            "longitude": 120.056285,
            "station_name": "西溪医院横街公交站",
            "station_seq": 6
          },
          {
            "id": "ca6dd877-fe78-4e0f-804f-470604df1d2a",
            "latitude": 30.238027,
            "longitude": 120.051897,
            "station_name": "1A区块/3号楼西侧",
            "station_seq": 7
          },
          {
            "id": "9b578c3d-8680-4595-9d03-6f840f8b4591",
            "latitude": 30.235733,
            "longitude": 120.047383,
            "station_name": "乌溪江路北口",
            "station_seq": 8
          },
          {
            "id": "d9cc56a0-1a5b-4d4a-a85e-f9cb3be28fc0",
            "latitude": 30.229598,
            "longitude": 120.039603,
            "station_name": "古运河路西口（图书馆西南侧）",
            "station_seq": 9
          },
          {
            "id": "fb42bfb1-4a0b-4bd6-9b27-17cee83230f5",
            "latitude": 30.230062,
            "longitude": 120.044001,
            "station_name": "语林楼",
            "station_seq": 10
          }
        ],
        "id": "a899298d-12ac-4fd6-b872-af1a5e11a714",
        "instance_days": 10,
        "is_active": true,
        "is_bluk_order_staff_level": false,
        "long_distance": false,
        "mtime": "2024-07-19 17:18:34",
        "net_mode": 0,
        "order_limit_minute": 120,
        "order_limit_on": true,
        "order_mode": 10,
        "order_mode_name": "预约模式",
        "other_price": {
          "student": 0,
          "student_ticket": 0,
          "teacher": 0
        },
        "overtime": false,
        "people_vehicle": false,
        "price": 0,
        "refund_at_dispath": false,
        "refund_at_dispath_limit_minute": 0,
        "remainder_remind": 0,
        "remind_admin": "[]",
        "reserved_seat": 0,
        "return_stations_json": [],
        "seats": 0,
        "shuttle_name": "9号线（莫干山-屏峰）",
        "sort_number": 14,
        "station_names": [],
        "stations_json": [
          {
            "id": "dde5e5e2-5eff-458b-ac15-84d117df7261",
            "latitude": 30.557927,
            "longitude": 120.036576,
            "station_name": "莫干山校区",
            "station_seq": 0
          },
          {
            "id": "b59d8ac2-437f-4617-8660-567ab4dd0009",
            "latitude": 30.31834,
            "longitude": 120.102251,
            "station_name": "华东陶瓷建材市场公交站",
            "station_seq": 1
          },
          {
            "id": "c0a451f2-1f5d-494b-a1c6-d2a80afebddb",
            "latitude": 30.305117,
            "longitude": 120.104439,
            "station_name": "三坝公交站",
            "station_seq": 2
          },
          {
            "id": "23d4a7ce-63c5-4de2-9313-0611d4e1a5c4",
            "latitude": 30.296188,
            "longitude": 120.104578,
            "station_name": "政新花园公交站",
            "station_seq": 3
          },
          {
            "id": "3877bdcc-7e73-4ab1-a35b-283a33790357",
            "latitude": 30.279816,
            "longitude": 120.10765,
            "station_name": "古墩路金月巷公交站",
            "station_seq": 4
          },
          {
            "id": "fab5f24e-f826-4e48-83ed-5537c10ea0bb",
            "latitude": 30.250428,
            "longitude": 120.059268,
            "station_name": "留下北公交站",
            "station_seq": 5
          },
          {
            "id": "ad257597-c56b-4451-b89c-869a6ad5a7c5",
            "latitude": 30.236814,
            "longitude": 120.056285,
            "station_name": "西溪医院横街公交站",
            "station_seq": 6
          },
          {
            "id": "ca6dd877-fe78-4e0f-804f-470604df1d2a",
            "latitude": 30.238027,
            "longitude": 120.051897,
            "station_name": "1A区块/3号楼西侧",
            "station_seq": 7
          },
          {
            "id": "9b578c3d-8680-4595-9d03-6f840f8b4591",
            "latitude": 30.235733,
            "longitude": 120.047383,
            "station_name": "乌溪江路北口",
            "station_seq": 8
          },
          {
            "id": "d9cc56a0-1a5b-4d4a-a85e-f9cb3be28fc0",
            "latitude": 30.229598,
            "longitude": 120.039603,
            "station_name": "古运河路西口（图书馆西南侧）",
            "station_seq": 9
          },
          {
            "id": "fb42bfb1-4a0b-4bd6-9b27-17cee83230f5",
            "latitude": 30.230062,
            "longitude": 120.044001,
            "station_name": "语林楼",
            "station_seq": 10
          }
        ],
        "ticket_check_minutes": 16,
        "ticket_of_buses": true
      },
      "shuttle_type": -10,
      "shuttle_type_name": "去程"
    },
    {
      "ctime": "2022-12-25 10:21:34",
      "departure_time": "20:30",
      "id": "0bd4a657-bd62-4c21-b5ed-11dd6665abee",
      "mtime": "2022-12-25 10:21:34",
      "punctuality_time": null,
      "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
      "shuttle_bus_vo": {
        "apply_dispatch_minutes": 0,
        "apply_expired_minutes": 16,
        "auto_dispatch": false,
        "bluk_order": false,
        "bluk_order_staff_levels": "[]",
        "bus_reminder": 30,
        "bus_times": [
          {
            "ctime": "2022-10-20 20:40:49",
            "departure_time": "06:40",
            "id": "1b192003-143c-4221-8148-176517e7e2fe",
            "mtime": "2022-10-20 20:40:49",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2023-01-05 09:57:52",
            "departure_time": "07:20",
            "id": "66a398e6-ce32-4d14-bd05-28002e24ecfd",
            "mtime": "2023-01-05 09:57:52",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:37",
            "departure_time": "08:00",
            "id": "4dba3520-2cb0-4c21-a743-78590ff20f0a",
            "mtime": "2022-10-20 21:40:37",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:37",
            "departure_time": "10:10",
            "id": "a7114208-2153-47ca-981e-04a5ecc70421",
            "mtime": "2022-10-20 21:40:37",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:47:14",
            "departure_time": "12:00",
            "id": "9eb822d3-c41f-43b3-b28e-9fe5e0efbda5",
            "mtime": "2022-10-20 21:47:14",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:37",
            "departure_time": "13:30",
            "id": "06dba5b3-1624-4917-8706-608061465bdf",
            "mtime": "2022-10-20 21:40:37",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-12-25 10:21:34",
            "departure_time": "16:30",
            "id": "8f329917-8c30-4d35-aa14-7e6265634f31",
            "mtime": "2022-12-25 10:21:34",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:47:14",
            "departure_time": "17:00",
            "id": "fa3e330b-1bae-4f50-9ebb-163af03981b9",
            "mtime": "2022-10-20 21:47:14",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:38",
            "departure_time": "17:30",
            "id": "542548a4-f98c-4c38-8bd1-de0c81d465e8",
            "mtime": "2022-10-20 21:40:38",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-12-25 10:21:34",
            "departure_time": "20:30",
            "id": "0bd4a657-bd62-4c21-b5ed-11dd6665abee",
            "mtime": "2022-12-25 10:21:34",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          },
          {
            "ctime": "2022-10-20 21:40:38",
            "departure_time": "21:30",
            "id": "f2b5cbcd-5657-4924-bf35-1dc208c6efea",
            "mtime": "2022-10-20 21:40:38",
            "punctuality_time": null,
            "shuttle_bus": "a899298d-12ac-4fd6-b872-af1a5e11a714",
            "shuttle_type": -10,
            "shuttle_type_name": "去程"
          }
        ],
        "check_mode": 20,
        "check_mode_name": "硬件检票",
        "ctime": "2022-10-20 20:40:49",
        "departure_time": "00:00",
        "driver_dispatch": false,
        "go_stations_json": [
          {
            "id": "dde5e5e2-5eff-458b-ac15-84d117df7261",
            "latitude": 30.557927,
            "longitude": 120.036576,
            "station_name": "莫干山校区",
            "station_seq": 0
          },
          {
            "id": "b59d8ac2-437f-4617-8660-567ab4dd0009",
            "latitude": 30.31834,
            "longitude": 120.102251,
            "station_name": "华东陶瓷建材市场公交站",
            "station_seq": 1
          },
          {
            "id": "c0a451f2-1f5d-494b-a1c6-d2a80afebddb",
            "latitude": 30.305117,
            "longitude": 120.104439,
            "station_name": "三坝公交站",
            "station_seq": 2
          },
          {
            "id": "23d4a7ce-63c5-4de2-9313-0611d4e1a5c4",
            "latitude": 30.296188,
            "longitude": 120.104578,
            "station_name": "政新花园公交站",
            "station_seq": 3
          },
          {
            "id": "3877bdcc-7e73-4ab1-a35b-283a33790357",
            "latitude": 30.279816,
            "longitude": 120.10765,
            "station_name": "古墩路金月巷公交站",
            "station_seq": 4
          },
          {
            "id": "fab5f24e-f826-4e48-83ed-5537c10ea0bb",
            "latitude": 30.250428,
            "longitude": 120.059268,
            "station_name": "留下北公交站",
            "station_seq": 5
          },
          {
            "id": "ad257597-c56b-4451-b89c-869a6ad5a7c5",
            "latitude": 30.236814,
            "longitude": 120.056285,
            "station_name": "西溪医院横街公交站",
            "station_seq": 6
          },
          {
            "id": "ca6dd877-fe78-4e0f-804f-470604df1d2a",
            "latitude": 30.238027,
            "longitude": 120.051897,
            "station_name": "1A区块/3号楼西侧",
            "station_seq": 7
          },
          {
            "id": "9b578c3d-8680-4595-9d03-6f840f8b4591",
            "latitude": 30.235733,
            "longitude": 120.047383,
            "station_name": "乌溪江路北口",
            "station_seq": 8
          },
          {
            "id": "d9cc56a0-1a5b-4d4a-a85e-f9cb3be28fc0",
            "latitude": 30.229598,
            "longitude": 120.039603,
            "station_name": "古运河路西口（图书馆西南侧）",
            "station_seq": 9
          },
          {
            "id": "fb42bfb1-4a0b-4bd6-9b27-17cee83230f5",
            "latitude": 30.230062,
            "longitude": 120.044001,
            "station_name": "语林楼",
            "station_seq": 10
          }
        ],
        "id": "a899298d-12ac-4fd6-b872-af1a5e11a714",
        "instance_days": 10,
        "is_active": true,
        "is_bluk_order_staff_level": false,
        "long_distance": false,
        "mtime": "2024-07-19 17:18:34",
        "net_mode": 0,
        "order_limit_minute": 120,
        "order_limit_on": true,
        "order_mode": 10,
        "order_mode_name": "预约模式",
        "other_price": {
          "student": 0,
          "student_ticket": 0,
          "teacher": 0
        },
        "overtime": false,
        "people_vehicle": false,
        "price": 0,
        "refund_at_dispath": false,
        "refund_at_dispath_limit_minute": 0,
        "remainder_remind": 0,
        "remind_admin": "[]",
        "reserved_seat": 0,
        "return_stations_json": [],
        "seats": 0,
        "shuttle_name": "9号线（莫干山-屏峰）",
        "sort_number": 14,
        "station_names": [],
        "stations_json": [
          {
            "id": "dde5e5e2-5eff-458b-ac15-84d117df7261",
            "latitude": 30.557927,
            "longitude": 120.036576,
            "station_name": "莫干山校区",
            "station_seq": 0
          },
          {
            "id": "b59d8ac2-437f-4617-8660-567ab4dd0009",
            "latitude": 30.31834,
            "longitude": 120.102251,
            "station_name": "华东陶瓷建材市场公交站",
            "station_seq": 1
          },
          {
            "id": "c0a451f2-1f5d-494b-a1c6-d2a80afebddb",
            "latitude": 30.305117,
            "longitude": 120.104439,
            "station_name": "三坝公交站",
            "station_seq": 2
          },
          {
            "id": "23d4a7ce-63c5-4de2-9313-0611d4e1a5c4",
            "latitude": 30.296188,
            "longitude": 120.104578,
            "station_name": "政新花园公交站",
            "station_seq": 3
          },
          {
            "id": "3877bdcc-7e73-4ab1-a35b-283a33790357",
            "latitude": 30.279816,
            "longitude": 120.10765,
            "station_name": "古墩路金月巷公交站",
            "station_seq": 4
          },
          {
            "id": "fab5f24e-f826-4e48-83ed-5537c10ea0bb",
            "latitude": 30.250428,
            "longitude": 120.059268,
            "station_name": "留下北公交站",
            "station_seq": 5
          },
          {
            "id": "ad257597-c56b-4451-b89c-869a6ad5a7c5",
            "latitude": 30.236814,
            "longitude": 120.056285,
            "station_name": "西溪医院横街公交站",
            "station_seq": 6
          },
          {
            "id": "ca6dd877-fe78-4e0f-804f-470604df1d2a",
            "latitude": 30.238027,
            "longitude": 120.051897,
            "station_name": "1A区块/3号楼西侧",
            "station_seq": 7
          },
          {
            "id": "9b578c3d-8680-4595-9d03-6f840f8b4591",
            "latitude": 30.235733,
            "longitude": 120.047383,
            "station_name": "乌溪江路北口",
            "station_seq": 8
          },
          {
            "id": "d9cc56a0-1a5b-4d4a-a85e-f9cb3be28fc0",
            "latitude": 30.229598,
            "longitude": 120.039603,
            "station_name": "古运河路西口（图书馆西南侧）",
            "station_seq": 9
          },
          {
            "id": "fb42bfb1-4a0b-4bd6-9b27-17cee83230f5",
            "latitude": 30.230062,
            "longitude": 120.044001,
            "station_name": "语林楼",
            "station_seq": 10
          }
        ],
        "ticket_check_minutes": 16,
        "ticket_of_buses": true
      },
      "shuttle_type": -10,
      "shuttle_type_name": "去程"
    }
  ],
  "message": "Success"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» data|[object]|true|none||none|
|»» ctime|string|true|none||none|
|»» departure_time|string|true|none||none|
|»» id|string|true|none||none|
|»» mtime|string|true|none||none|
|»» punctuality_time|null|true|none||none|
|»» shuttle_bus|string|true|none||none|
|»» shuttle_bus_vo|object|true|none||none|
|»»» apply_dispatch_minutes|integer|true|none||none|
|»»» apply_expired_minutes|integer|true|none||none|
|»»» auto_dispatch|boolean|true|none||none|
|»»» bluk_order|boolean|true|none||none|
|»»» bluk_order_staff_levels|string|true|none||none|
|»»» bus_reminder|integer|true|none||none|
|»»» bus_times|[object]|true|none||none|
|»»»» ctime|string|true|none||none|
|»»»» departure_time|string|true|none||none|
|»»»» id|string|true|none||none|
|»»»» mtime|string|true|none||none|
|»»»» punctuality_time|null|true|none||none|
|»»»» shuttle_bus|string|true|none||none|
|»»»» shuttle_type|integer|true|none||none|
|»»»» shuttle_type_name|string|true|none||none|
|»»» check_mode|integer|true|none||none|
|»»» check_mode_name|string|true|none||none|
|»»» ctime|string|true|none||none|
|»»» departure_time|string|true|none||none|
|»»» driver_dispatch|boolean|true|none||none|
|»»» go_stations_json|[object]|true|none||none|
|»»»» id|string|true|none||none|
|»»»» latitude|number|true|none||none|
|»»»» longitude|number|true|none||none|
|»»»» station_name|string|true|none||none|
|»»»» station_seq|integer|true|none||none|
|»»» id|string|true|none||none|
|»»» instance_days|integer|true|none||none|
|»»» is_active|boolean|true|none||none|
|»»» is_bluk_order_staff_level|boolean|true|none||none|
|»»» long_distance|boolean|true|none||none|
|»»» mtime|string|true|none||none|
|»»» net_mode|integer|true|none||none|
|»»» order_limit_minute|integer|true|none||none|
|»»» order_limit_on|boolean|true|none||none|
|»»» order_mode|integer|true|none||none|
|»»» order_mode_name|string|true|none||none|
|»»» other_price|object|true|none||none|
|»»»» student|integer|true|none||none|
|»»»» student_ticket|integer|true|none||none|
|»»»» teacher|integer|true|none||none|
|»»» overtime|boolean|true|none||none|
|»»» people_vehicle|boolean|true|none||none|
|»»» price|integer|true|none||none|
|»»» refund_at_dispath|boolean|true|none||none|
|»»» refund_at_dispath_limit_minute|integer|true|none||none|
|»»» remainder_remind|integer|true|none||none|
|»»» remind_admin|string|true|none||none|
|»»» reserved_seat|integer|true|none||none|
|»»» return_stations_json|[string]|true|none||none|
|»»» seats|integer|true|none||none|
|»»» shuttle_name|string|true|none||none|
|»»» sort_number|integer|true|none||none|
|»»» station_names|[string]|true|none||none|
|»»» stations_json|[object]|true|none||none|
|»»»» id|string|true|none||none|
|»»»» latitude|number|true|none||none|
|»»»» longitude|number|true|none||none|
|»»»» station_name|string|true|none||none|
|»»»» station_seq|integer|true|none||none|
|»»» ticket_check_minutes|integer|true|none||none|
|»»» ticket_of_buses|boolean|true|none||none|
|»» shuttle_type|integer|true|none||none|
|»» shuttle_type_name|string|true|none||none|
|» message|string|true|none||none|

## POST 预约班车

POST /api/bus/book

> Body 请求参数

```json
{
  "bus_date": "string",
  "bus_station": "string"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Authorization|header|string| 否 |none|
|body|body|object| 否 |none|
|» bus_date|body|string| 是 |none|
|» bus_station|body|string| 是 |none|

> 返回示例

> 成功

```json
{
  "code": 404,
  "data": null,
  "message": "该班次已购买"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|number|true|none||none|
|» message|string|true|none||none|
|» data|object|true|none||none|

## GET 获取预约记录

GET /api/bus/bookrecord

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|page|query|number| 否 |none|
|page_size|query|number| 否 |none|
|status|query|string| 否 |none|
|Authorization|header|string| 否 |none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "data": [
    {
      "admin": null,
      "approval_status": 0,
      "boarding_station": null,
      "busdriver": null,
      "busfavourite": true,
      "busvehicle": null,
      "car_flag": "string",
      "check_time": null,
      "checkin_type": 0,
      "ctime": "string",
      "departure_datetime": "string",
      "driver_name": null,
      "driver_phone": null,
      "has_ticket": true,
      "id": "string",
      "is_commit": true,
      "mtime": "string",
      "pay_amount": 0,
      "pay_time": "string",
      "pay_type": "string",
      "reason": null,
      "shuttle_bus": "string",
      "shuttle_bus_date_vo": {
        "apply_dispatch_datetime": "string",
        "apply_expired_datetime": "string",
        "clock_time": null,
        "ctime": "string",
        "departure_date": "string",
        "departure_datetime": "string",
        "dispatch_status_name": "string",
        "dispath_status": 0,
        "extra_order_push": null,
        "id": "string",
        "mtime": "string",
        "price": 0,
        "remaining_seats": 0,
        "seats": 0,
        "shuttle_bus": "string",
        "shuttle_bus_time": "string",
        "shuttle_bus_time_vo": {
          "ctime": "string",
          "departure_time": "string",
          "id": "string",
          "mtime": "string",
          "punctuality_time": null,
          "shuttle_bus": "string",
          "shuttle_bus_vo": {},
          "shuttle_type": 0,
          "shuttle_type_name": "string"
        },
        "shuttle_bus_vo": {
          "apply_dispatch_minutes": 0,
          "apply_expired_minutes": 0,
          "auto_dispatch": true,
          "bluk_order": true,
          "bluk_order_staff_levels": "string",
          "bus_reminder": 0,
          "check_mode": 0,
          "check_mode_name": "string",
          "ctime": "string",
          "departure_time": "string",
          "driver_dispatch": true,
          "go_stations_json": [
            null
          ],
          "id": "string",
          "instance_days": 0,
          "is_active": true,
          "is_bluk_order_staff_level": true,
          "long_distance": true,
          "mtime": "string",
          "net_mode": 0,
          "order_limit_minute": 0,
          "order_limit_on": true,
          "order_mode": 0,
          "order_mode_name": "string",
          "other_price": "string",
          "overtime": true,
          "people_vehicle": true,
          "price": 0,
          "refund_at_dispath": true,
          "refund_at_dispath_limit_minute": 0,
          "remainder_remind": 0,
          "remind_admin": "string",
          "reserved_seat": 0,
          "return_stations_json": [
            null
          ],
          "seats": 0,
          "shuttle_name": "string",
          "sort_number": 0,
          "station_names": "string",
          "stations_json": [
            null
          ],
          "ticket_check_minutes": 0,
          "ticket_of_buses": true
        },
        "shuttle_name": "string",
        "station_names": "string",
        "stations_json": [
          {
            "num": null,
            "station_name": null,
            "station_seq": null
          }
        ],
        "status": 0,
        "status_name": "string",
        "ticket_check_datetime": "string"
      },
      "shuttle_bus_id": "string",
      "shuttle_type": "string",
      "status": 0,
      "status_name": "string",
      "vehicle_no": null
    }
  ],
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» data|[object]|true|none||none|
|»» admin|null|false|none||none|
|»» approval_status|integer|false|none||none|
|»» boarding_station|null|false|none||none|
|»» busdriver|null|false|none||none|
|»» busfavourite|boolean|false|none||none|
|»» busvehicle|null|false|none||none|
|»» car_flag|string|false|none||none|
|»» check_time|null|false|none||none|
|»» checkin_type|integer|false|none||none|
|»» ctime|string|false|none||none|
|»» departure_datetime|string|false|none||none|
|»» driver_name|null|false|none||none|
|»» driver_phone|null|false|none||none|
|»» has_ticket|boolean|false|none||none|
|»» id|string|false|none||none|
|»» is_commit|boolean|false|none||none|
|»» mtime|string|false|none||none|
|»» pay_amount|integer|false|none||none|
|»» pay_time|string|false|none||none|
|»» pay_type|string|false|none||none|
|»» reason|null|false|none||none|
|»» shuttle_bus|string|false|none||none|
|»» shuttle_bus_date_vo|object|false|none||none|
|»»» apply_dispatch_datetime|string|true|none||none|
|»»» apply_expired_datetime|string|true|none||none|
|»»» clock_time|null|true|none||none|
|»»» ctime|string|true|none||none|
|»»» departure_date|string|true|none||none|
|»»» departure_datetime|string|true|none||none|
|»»» dispatch_status_name|string|true|none||none|
|»»» dispath_status|integer|true|none||none|
|»»» extra_order_push|null|true|none||none|
|»»» id|string|true|none||none|
|»»» mtime|string|true|none||none|
|»»» price|integer|true|none||none|
|»»» remaining_seats|integer|true|none||none|
|»»» seats|integer|true|none||none|
|»»» shuttle_bus|string|true|none||none|
|»»» shuttle_bus_time|string|true|none||none|
|»»» shuttle_bus_time_vo|object|true|none||none|
|»»»» ctime|string|true|none||none|
|»»»» departure_time|string|true|none||none|
|»»»» id|string|true|none||none|
|»»»» mtime|string|true|none||none|
|»»»» punctuality_time|null|true|none||none|
|»»»» shuttle_bus|string|true|none||none|
|»»»» shuttle_bus_vo|object|true|none||none|
|»»»»» apply_dispatch_minutes|integer|true|none||none|
|»»»»» apply_expired_minutes|integer|true|none||none|
|»»»»» auto_dispatch|boolean|true|none||none|
|»»»»» bluk_order|boolean|true|none||none|
|»»»»» bluk_order_staff_levels|string|true|none||none|
|»»»»» bus_reminder|integer|true|none||none|
|»»»»» check_mode|integer|true|none||none|
|»»»»» check_mode_name|string|true|none||none|
|»»»»» ctime|string|true|none||none|
|»»»»» departure_time|string|true|none||none|
|»»»»» driver_dispatch|boolean|true|none||none|
|»»»»» go_stations_json|[object]|true|none||none|
|»»»»»» id|string|true|none||none|
|»»»»»» latitude|number|true|none||none|
|»»»»»» longitude|number|true|none||none|
|»»»»»» station_name|string|true|none||none|
|»»»»»» station_seq|integer|true|none||none|
|»»»»» id|string|true|none||none|
|»»»»» instance_days|integer|true|none||none|
|»»»»» is_active|boolean|true|none||none|
|»»»»» is_bluk_order_staff_level|boolean|true|none||none|
|»»»»» long_distance|boolean|true|none||none|
|»»»»» mtime|string|true|none||none|
|»»»»» net_mode|integer|true|none||none|
|»»»»» order_limit_minute|integer|true|none||none|
|»»»»» order_limit_on|boolean|true|none||none|
|»»»»» order_mode|integer|true|none||none|
|»»»»» order_mode_name|string|true|none||none|
|»»»»» other_price|string|true|none||none|
|»»»»» overtime|boolean|true|none||none|
|»»»»» people_vehicle|boolean|true|none||none|
|»»»»» price|integer|true|none||none|
|»»»»» refund_at_dispath|boolean|true|none||none|
|»»»»» refund_at_dispath_limit_minute|integer|true|none||none|
|»»»»» remainder_remind|integer|true|none||none|
|»»»»» remind_admin|string|true|none||none|
|»»»»» reserved_seat|integer|true|none||none|
|»»»»» return_stations_json|[string]|true|none||none|
|»»»»» seats|integer|true|none||none|
|»»»»» shuttle_name|string|true|none||none|
|»»»»» sort_number|integer|true|none||none|
|»»»»» station_names|string|true|none||none|
|»»»»» stations_json|[string]|true|none||none|
|»»»»» ticket_check_minutes|integer|true|none||none|
|»»»»» ticket_of_buses|boolean|true|none||none|
|»»»» shuttle_type|integer|true|none||none|
|»»»» shuttle_type_name|string|true|none||none|
|»»» shuttle_bus_vo|object|true|none||none|
|»»»» apply_dispatch_minutes|integer|true|none||none|
|»»»» apply_expired_minutes|integer|true|none||none|
|»»»» auto_dispatch|boolean|true|none||none|
|»»»» bluk_order|boolean|true|none||none|
|»»»» bluk_order_staff_levels|string|true|none||none|
|»»»» bus_reminder|integer|true|none||none|
|»»»» check_mode|integer|true|none||none|
|»»»» check_mode_name|string|true|none||none|
|»»»» ctime|string|true|none||none|
|»»»» departure_time|string|true|none||none|
|»»»» driver_dispatch|boolean|true|none||none|
|»»»» go_stations_json|[object]|true|none||none|
|»»»»» id|string|true|none||none|
|»»»»» latitude|number|true|none||none|
|»»»»» longitude|number|true|none||none|
|»»»»» station_name|string|true|none||none|
|»»»»» station_seq|integer|true|none||none|
|»»»» id|string|true|none||none|
|»»»» instance_days|integer|true|none||none|
|»»»» is_active|boolean|true|none||none|
|»»»» is_bluk_order_staff_level|boolean|true|none||none|
|»»»» long_distance|boolean|true|none||none|
|»»»» mtime|string|true|none||none|
|»»»» net_mode|integer|true|none||none|
|»»»» order_limit_minute|integer|true|none||none|
|»»»» order_limit_on|boolean|true|none||none|
|»»»» order_mode|integer|true|none||none|
|»»»» order_mode_name|string|true|none||none|
|»»»» other_price|string|true|none||none|
|»»»» overtime|boolean|true|none||none|
|»»»» people_vehicle|boolean|true|none||none|
|»»»» price|integer|true|none||none|
|»»»» refund_at_dispath|boolean|true|none||none|
|»»»» refund_at_dispath_limit_minute|integer|true|none||none|
|»»»» remainder_remind|integer|true|none||none|
|»»»» remind_admin|string|true|none||none|
|»»»» reserved_seat|integer|true|none||none|
|»»»» return_stations_json|[string]|true|none||none|
|»»»» seats|integer|true|none||none|
|»»»» shuttle_name|string|true|none||none|
|»»»» sort_number|integer|true|none||none|
|»»»» station_names|string|true|none||none|
|»»»» stations_json|[string]|true|none||none|
|»»»» ticket_check_minutes|integer|true|none||none|
|»»»» ticket_of_buses|boolean|true|none||none|
|»»» shuttle_name|string|true|none||none|
|»»» station_names|string|true|none||none|
|»»» stations_json|[object]|true|none||none|
|»»»» num|integer|true|none||none|
|»»»» station_name|string|true|none||none|
|»»»» station_seq|integer|true|none||none|
|»»» status|integer|true|none||none|
|»»» status_name|string|true|none||none|
|»»» ticket_check_datetime|string|true|none||none|
|»» shuttle_bus_id|string|false|none||none|
|»» shuttle_type|string|false|none||none|
|»» status|integer|false|none||none|
|»» status_name|string|false|none||none|
|»» vehicle_no|null|false|none||none|
|» message|string|true|none||none|

## GET 查询班次信息

GET /api/bus/date

> Body 请求参数

```json
{
  "bus_time": "string",
  "bus_id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Authorization|header|string| 否 |none|
|body|body|object| 否 |none|
|» bus_time|body|string| 是 |none|
|» bus_id|body|string| 是 |none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "data": [
    {
      "apply_dispatch_datetime": "string",
      "apply_expired_datetime": "string",
      "clock_time": null,
      "ctime": "string",
      "departure_date": "string",
      "departure_datetime": "string",
      "dispatch_status_name": "string",
      "dispath_status": 0,
      "extra_bus": {
        "apply": true,
        "extra_bus_config": true,
        "extra_bus_order_cancel": true,
        "extra_bus_order_id": null,
        "inform_admin_ids": [
          "string"
        ],
        "num": 0
      },
      "extra_order_push": null,
      "id": "string",
      "mtime": "string",
      "order_cnt": 0,
      "order_status": 0,
      "price": 0,
      "punishment": true,
      "remaining_seats": 0,
      "reserved_seat": 0,
      "seats": 0,
      "shuttle_bus": "string",
      "shuttle_bus_time": "string",
      "shuttle_bus_time_vo": {
        "ctime": "string",
        "departure_time": "string",
        "id": "string",
        "mtime": "string",
        "punctuality_time": null,
        "shuttle_bus": "string",
        "shuttle_bus_vo": {
          "apply_dispatch_minutes": 0,
          "apply_expired_minutes": 0,
          "auto_dispatch": true,
          "bluk_order": true,
          "bluk_order_staff_levels": "string",
          "bus_reminder": 0,
          "bus_times": [
            null
          ],
          "check_mode": 0,
          "check_mode_name": "string",
          "ctime": "string",
          "departure_time": "string",
          "driver_dispatch": true,
          "go_stations_json": [
            null
          ],
          "id": "string",
          "instance_days": 0,
          "is_active": true,
          "is_bluk_order_staff_level": true,
          "long_distance": true,
          "mtime": "string",
          "net_mode": 0,
          "order_limit_minute": 0,
          "order_limit_on": true,
          "order_mode": 0,
          "order_mode_name": "string",
          "other_price": {},
          "overtime": true,
          "people_vehicle": true,
          "price": 0,
          "refund_at_dispath": true,
          "refund_at_dispath_limit_minute": 0,
          "remainder_remind": 0,
          "remind_admin": "string",
          "reserved_seat": 0,
          "return_stations_json": [
            null
          ],
          "seats": 0,
          "shuttle_name": "string",
          "sort_number": 0,
          "station_names": [
            null
          ],
          "stations_json": [
            null
          ],
          "ticket_check_minutes": 0,
          "ticket_of_buses": true
        },
        "shuttle_type": 0,
        "shuttle_type_name": "string"
      },
      "shuttle_bus_vo": {
        "apply_dispatch_minutes": 0,
        "apply_expired_minutes": 0,
        "auto_dispatch": true,
        "bluk_order": true,
        "bluk_order_staff_levels": "string",
        "bus_reminder": 0,
        "bus_times": [
          {
            "ctime": null,
            "departure_time": null,
            "id": null,
            "mtime": null,
            "punctuality_time": null,
            "shuttle_bus": null,
            "shuttle_type": null,
            "shuttle_type_name": null
          }
        ],
        "check_mode": 0,
        "check_mode_name": "string",
        "ctime": "string",
        "departure_time": "string",
        "driver_dispatch": true,
        "go_stations_json": [
          {
            "id": null,
            "latitude": null,
            "longitude": null,
            "station_name": null,
            "station_seq": null
          }
        ],
        "id": "string",
        "instance_days": 0,
        "is_active": true,
        "is_bluk_order_staff_level": true,
        "long_distance": true,
        "mtime": "string",
        "net_mode": 0,
        "order_limit_minute": 0,
        "order_limit_on": true,
        "order_mode": 0,
        "order_mode_name": "string",
        "other_price": {
          "student": 0,
          "student_ticket": 0,
          "teacher": 0
        },
        "overtime": true,
        "people_vehicle": true,
        "price": 0,
        "refund_at_dispath": true,
        "refund_at_dispath_limit_minute": 0,
        "remainder_remind": 0,
        "remind_admin": "string",
        "reserved_seat": 0,
        "return_stations_json": [
          "string"
        ],
        "seats": 0,
        "shuttle_name": "string",
        "sort_number": 0,
        "station_names": [
          "string"
        ],
        "stations_json": [
          {
            "id": null,
            "latitude": null,
            "longitude": null,
            "station_name": null,
            "station_seq": null
          }
        ],
        "ticket_check_minutes": 0,
        "ticket_of_buses": true
      },
      "shuttle_name": "string",
      "station_names": "string",
      "stations_json": [
        {
          "id": "string",
          "station_name": "string",
          "station_seq": 0
        }
      ],
      "status": 0,
      "status_name": "string",
      "ticket_check_datetime": "string"
    }
  ],
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» data|[object]|true|none||none|
|»» apply_dispatch_datetime|string|false|none||none|
|»» apply_expired_datetime|string|false|none||none|
|»» clock_time|null|false|none||none|
|»» ctime|string|false|none||none|
|»» departure_date|string|false|none||none|
|»» departure_datetime|string|false|none||none|
|»» dispatch_status_name|string|false|none||none|
|»» dispath_status|integer|false|none||none|
|»» extra_bus|object|false|none||none|
|»»» apply|boolean|true|none||none|
|»»» extra_bus_config|boolean|true|none||none|
|»»» extra_bus_order_cancel|boolean|true|none||none|
|»»» extra_bus_order_id|null|true|none||none|
|»»» inform_admin_ids|[string]|true|none||none|
|»»» num|integer|true|none||none|
|»» extra_order_push|null|false|none||none|
|»» id|string|false|none||none|
|»» mtime|string|false|none||none|
|»» order_cnt|integer|false|none||none|
|»» order_status|integer|false|none||none|
|»» price|integer|false|none||none|
|»» punishment|boolean|false|none||none|
|»» remaining_seats|integer|false|none||none|
|»» reserved_seat|integer|false|none||none|
|»» seats|integer|false|none||none|
|»» shuttle_bus|string|false|none||none|
|»» shuttle_bus_time|string|false|none||none|
|»» shuttle_bus_time_vo|object|false|none||none|
|»»» ctime|string|true|none||none|
|»»» departure_time|string|true|none||none|
|»»» id|string|true|none||none|
|»»» mtime|string|true|none||none|
|»»» punctuality_time|null|true|none||none|
|»»» shuttle_bus|string|true|none||none|
|»»» shuttle_bus_vo|object|true|none||none|
|»»»» apply_dispatch_minutes|integer|true|none||none|
|»»»» apply_expired_minutes|integer|true|none||none|
|»»»» auto_dispatch|boolean|true|none||none|
|»»»» bluk_order|boolean|true|none||none|
|»»»» bluk_order_staff_levels|string|true|none||none|
|»»»» bus_reminder|integer|true|none||none|
|»»»» bus_times|[object]|true|none||none|
|»»»»» ctime|string|true|none||none|
|»»»»» departure_time|string|true|none||none|
|»»»»» id|string|true|none||none|
|»»»»» mtime|string|true|none||none|
|»»»»» punctuality_time|null|true|none||none|
|»»»»» shuttle_bus|string|true|none||none|
|»»»»» shuttle_type|integer|true|none||none|
|»»»»» shuttle_type_name|string|true|none||none|
|»»»» check_mode|integer|true|none||none|
|»»»» check_mode_name|string|true|none||none|
|»»»» ctime|string|true|none||none|
|»»»» departure_time|string|true|none||none|
|»»»» driver_dispatch|boolean|true|none||none|
|»»»» go_stations_json|[object]|true|none||none|
|»»»»» id|string|true|none||none|
|»»»»» latitude|number|true|none||none|
|»»»»» longitude|number|true|none||none|
|»»»»» station_name|string|true|none||none|
|»»»»» station_seq|integer|true|none||none|
|»»»» id|string|true|none||none|
|»»»» instance_days|integer|true|none||none|
|»»»» is_active|boolean|true|none||none|
|»»»» is_bluk_order_staff_level|boolean|true|none||none|
|»»»» long_distance|boolean|true|none||none|
|»»»» mtime|string|true|none||none|
|»»»» net_mode|integer|true|none||none|
|»»»» order_limit_minute|integer|true|none||none|
|»»»» order_limit_on|boolean|true|none||none|
|»»»» order_mode|integer|true|none||none|
|»»»» order_mode_name|string|true|none||none|
|»»»» other_price|object|true|none||none|
|»»»»» student|integer|true|none||none|
|»»»»» student_ticket|integer|true|none||none|
|»»»»» teacher|integer|true|none||none|
|»»»» overtime|boolean|true|none||none|
|»»»» people_vehicle|boolean|true|none||none|
|»»»» price|integer|true|none||none|
|»»»» refund_at_dispath|boolean|true|none||none|
|»»»» refund_at_dispath_limit_minute|integer|true|none||none|
|»»»» remainder_remind|integer|true|none||none|
|»»»» remind_admin|string|true|none||none|
|»»»» reserved_seat|integer|true|none||none|
|»»»» return_stations_json|[string]|true|none||none|
|»»»» seats|integer|true|none||none|
|»»»» shuttle_name|string|true|none||none|
|»»»» sort_number|integer|true|none||none|
|»»»» station_names|[string]|true|none||none|
|»»»» stations_json|[object]|true|none||none|
|»»»»» id|string|true|none||none|
|»»»»» latitude|number|true|none||none|
|»»»»» longitude|number|true|none||none|
|»»»»» station_name|string|true|none||none|
|»»»»» station_seq|integer|true|none||none|
|»»»» ticket_check_minutes|integer|true|none||none|
|»»»» ticket_of_buses|boolean|true|none||none|
|»»» shuttle_type|integer|true|none||none|
|»»» shuttle_type_name|string|true|none||none|
|»» shuttle_bus_vo|object|false|none||none|
|»»» apply_dispatch_minutes|integer|true|none||none|
|»»» apply_expired_minutes|integer|true|none||none|
|»»» auto_dispatch|boolean|true|none||none|
|»»» bluk_order|boolean|true|none||none|
|»»» bluk_order_staff_levels|string|true|none||none|
|»»» bus_reminder|integer|true|none||none|
|»»» bus_times|[object]|true|none||none|
|»»»» ctime|string|true|none||none|
|»»»» departure_time|string|true|none||none|
|»»»» id|string|true|none||none|
|»»»» mtime|string|true|none||none|
|»»»» punctuality_time|null|true|none||none|
|»»»» shuttle_bus|string|true|none||none|
|»»»» shuttle_type|integer|true|none||none|
|»»»» shuttle_type_name|string|true|none||none|
|»»» check_mode|integer|true|none||none|
|»»» check_mode_name|string|true|none||none|
|»»» ctime|string|true|none||none|
|»»» departure_time|string|true|none||none|
|»»» driver_dispatch|boolean|true|none||none|
|»»» go_stations_json|[object]|true|none||none|
|»»»» id|string|true|none||none|
|»»»» latitude|number|true|none||none|
|»»»» longitude|number|true|none||none|
|»»»» station_name|string|true|none||none|
|»»»» station_seq|integer|true|none||none|
|»»» id|string|true|none||none|
|»»» instance_days|integer|true|none||none|
|»»» is_active|boolean|true|none||none|
|»»» is_bluk_order_staff_level|boolean|true|none||none|
|»»» long_distance|boolean|true|none||none|
|»»» mtime|string|true|none||none|
|»»» net_mode|integer|true|none||none|
|»»» order_limit_minute|integer|true|none||none|
|»»» order_limit_on|boolean|true|none||none|
|»»» order_mode|integer|true|none||none|
|»»» order_mode_name|string|true|none||none|
|»»» other_price|object|true|none||none|
|»»»» student|integer|true|none||none|
|»»»» student_ticket|integer|true|none||none|
|»»»» teacher|integer|true|none||none|
|»»» overtime|boolean|true|none||none|
|»»» people_vehicle|boolean|true|none||none|
|»»» price|integer|true|none||none|
|»»» refund_at_dispath|boolean|true|none||none|
|»»» refund_at_dispath_limit_minute|integer|true|none||none|
|»»» remainder_remind|integer|true|none||none|
|»»» remind_admin|string|true|none||none|
|»»» reserved_seat|integer|true|none||none|
|»»» return_stations_json|[string]|true|none||none|
|»»» seats|integer|true|none||none|
|»»» shuttle_name|string|true|none||none|
|»»» sort_number|integer|true|none||none|
|»»» station_names|[string]|true|none||none|
|»»» stations_json|[object]|true|none||none|
|»»»» id|string|true|none||none|
|»»»» latitude|number|true|none||none|
|»»»» longitude|number|true|none||none|
|»»»» station_name|string|true|none||none|
|»»»» station_seq|integer|true|none||none|
|»»» ticket_check_minutes|integer|true|none||none|
|»»» ticket_of_buses|boolean|true|none||none|
|»» shuttle_name|string|false|none||none|
|»» station_names|string|false|none||none|
|»» stations_json|[object]|false|none||none|
|»»» id|string|true|none||none|
|»»» station_name|string|true|none||none|
|»»» station_seq|integer|true|none||none|
|»» status|integer|false|none||none|
|»» status_name|string|false|none||none|
|»» ticket_check_datetime|string|false|none||none|
|» message|string|true|none||none|

## POST 取消预约

POST /api/bus/cancelbook

> Body 请求参数

```json
{
  "id": "string"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Authorization|header|string| 否 |none|
|body|body|object| 否 |none|
|» id|body|string| 是 |none|

> 返回示例

> 200 Response

```json
{
  "code": 0,
  "message": "string",
  "data": {}
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|number|true|none||none|
|» message|string|true|none||none|
|» data|object|true|none||none|

# user

## GET 获取二维码

GET /api/user/qrcode

> Body 请求参数

```json
{
  "openid": "string"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|Authorization|header|string| 否 |none|
|body|body|object| 否 |none|
|» openid|body|string| 是 |none|

> 返回示例

> 成功

```json
{
  "code": 200,
  "data": {
    "qrcode": "QG5ItCkkdbE8Qad4HvrK53bzY+X8U4EkacJTrXMLfD8pKOV98wrZKNEo4xDA/KB8Q6I3xuMGTp5ydUT2pIFJjw=="
  },
  "message": "Success"
}
```

```json
{
  "code": 200,
  "data": {
    "qrcode": "QG5ItCkkdbE8Qad4HvrK53bzY+X8U4EkacJTrXMLfD8pKOV98wrZKLQkWkrPLPpC4ImKrYOGmwNydUT2pIFJjw=="
  },
  "message": "Success"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» data|object|true|none||none|
|»» qrcode|string|true|none||none|
|» message|string|true|none||none|

## GET 获取学校信息

GET /api/user/company

> Body 请求参数

```json
{
  "password": "string",
  "phone": "string"
}
```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» password|body|string| 是 |none|
|» phone|body|string| 是 |none|

> 返回示例

> 成功

```json
{
  "code": 200,
  "data": {
    "company_name": "浙江工业大学",
    "id": "551ca035-4c97-4af4-96b5-a64e3320a6d9"
  },
  "message": "Success"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» data|object|true|none||none|
|»» company_name|string|true|none||none|
|»» id|string|true|none||none|
|» message|string|true|none||none|

# 数据模型

