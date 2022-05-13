# 说明文档


### Google Cloud Functions 设置
* Python version: 3.8
* requests version:  2.25.1
* Entry point：  triggered_pubsub 或者 triggered_http

### 环境变量 设置
* WEBHOOK_URL = "http://xxxx"
* PROM_USER = ""
* PROM_PWD = ""


### 触发方式 设置
* HTTP triggered_http
* Pub/Sub triggered_pubsub


### 注意事项 
如果使用triggered_http设置Authentication  Allow unauthenticated invocations


## 实施步骤

### 第一步 创建 Google Cloud Functions
<img width="1755" alt="image" src="https://user-images.githubusercontent.com/10955940/168231211-5d4d1b07-4193-4a05-a69b-22cd785b420b.png">


### 第二步 设置环境变量
<img width="1716" alt="image" src="https://user-images.githubusercontent.com/10955940/168217884-49110adb-8338-4f03-9e26-f430f645aba3.png">

### 第三步 复制代码
1. main.py
2. requirements.txt
3. 选择 runtime  python 3.8
4. 设置 Entry point  为 triggered_http 

<img width="1759" alt="image" src="https://user-images.githubusercontent.com/10955940/168232400-57ff6f72-efa4-4a0c-bb00-7cc7d112b342.png">


### 第四步 部署
点击 deploy 即可




### 第五步 

##### 创建Subscriptions  选择 push 方式 并关联 Google Cloud Functions 创建的 HTTP Triggered 并处理消息

![image](https://user-images.githubusercontent.com/10955940/167328637-36a53abc-40be-4ca1-95d1-323c4ac77dc2.png)
![image](https://user-images.githubusercontent.com/10955940/167328650-46980969-623d-4a41-a609-ae76d2a9cad0.png)

#####  创建Subscriptions  选择 pull 方式 并管理 Google Cloud Functions 创建的 Pub/Sub Triggered 并处理消息

<img width="1749" alt="image" src="https://user-images.githubusercontent.com/10955940/168234552-1f5816d4-b196-42a7-8fa3-595dd395cf37.png">


创建订阅
<img width="1744" alt="image" src="https://user-images.githubusercontent.com/10955940/167820477-34ce85e6-0fef-4652-aed9-664d50f8775f.png">
<img width="1743" alt="image" src="https://user-images.githubusercontent.com/10955940/167820823-d68605d0-59ec-4e9f-bf57-fa2c014df4af.png">

### 消息体
```json
{
  '@type': 'type.googleapis.com/google.pubsub.v1.PubsubMessage',
  'attributes': {
    'logging.googleapis.com/timestamp': '2022-05-11T06:09:00.527145Z'
  },
  'data': 'eyJpbnNlcnRJZCI6Ii15NDRlemplNnk3aXciLCJsb2dOYW1lIjoicHJvamVjdHMvc3BvdG9uLXByb2plY3QvbG9ncy9jbG91ZGF1ZGl0Lmdvb2dsZWFwaXMuY29tJTJGYWN0aXZpdHkiLCJvcGVyYXRpb24iOnsiZmlyc3QiOnRydWUsImlkIjoib3BlcmF0aW9uLTE2NTIyNDkzNDA0MzYtNWRlYjY0NzA0NjEzMi1hYzMxMTdlYS0wNzhmZjMzMyIsInByb2R1Y2VyIjoiY29tcHV0ZS5nb29nbGVhcGlzLmNvbSJ9LCJwcm90b1BheWxvYWQiOnsiQHR5cGUiOiJ0eXBlLmdvb2dsZWFwaXMuY29tL2dvb2dsZS5jbG91ZC5hdWRpdC5BdWRpdExvZyIsImF1dGhlbnRpY2F0aW9uSW5mbyI6eyJwcmluY2lwYWxFbWFpbCI6InpoYW5neWFuYm9AeXVuaW9uLWhrLmNvbSJ9LCJhdXRob3JpemF0aW9uSW5mbyI6W3siZ3JhbnRlZCI6dHJ1ZSwicGVybWlzc2lvbiI6ImNvbXB1dGUuaW5zdGFuY2VzLnN0b3AiLCJyZXNvdXJjZUF0dHJpYnV0ZXMiOnsibmFtZSI6InByb2plY3RzL3Nwb3Rvbi1wcm9qZWN0L3pvbmVzL3VzLXdlc3QxLWIvaW5zdGFuY2VzL3l3dC10ZXN0LWluc3RhbmNlMyIsInNlcnZpY2UiOiJjb21wdXRlIiwidHlwZSI6ImNvbXB1dGUuaW5zdGFuY2VzIn19XSwibWV0aG9kTmFtZSI6InYxLmNvbXB1dGUuaW5zdGFuY2VzLnN0b3AiLCJyZXF1ZXN0Ijp7IkB0eXBlIjoidHlwZS5nb29nbGVhcGlzLmNvbS9jb21wdXRlLmluc3RhbmNlcy5zdG9wIn0sInJlcXVlc3RNZXRhZGF0YSI6eyJjYWxsZXJJcCI6IjE2Ny4xNzkuNjguMjMiLCJjYWxsZXJTdXBwbGllZFVzZXJBZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDEuMC40OTUxLjQxIFNhZmFyaS81MzcuMzYsZ3ppcChnZmUpLGd6aXAoZ2ZlKSIsImRlc3RpbmF0aW9uQXR0cmlidXRlcyI6e30sInJlcXVlc3RBdHRyaWJ1dGVzIjp7ImF1dGgiOnt9LCJyZWFzb24iOiI4dVN5d0FZUUdnNURiMnhwYzJWMWJTQkdiRzkzY3ciLCJ0aW1lIjoiMjAyMi0wNS0xMVQwNjowOTowMC44Mzc1NjVaIn19LCJyZXNvdXJjZUxvY2F0aW9uIjp7ImN1cnJlbnRMb2NhdGlvbnMiOlsidXMtd2VzdDEtYiJdfSwicmVzb3VyY2VOYW1lIjoicHJvamVjdHMvc3BvdG9uLXByb2plY3Qvem9uZXMvdXMtd2VzdDEtYi9pbnN0YW5jZXMveXd0LXRlc3QtaW5zdGFuY2UzIiwicmVzcG9uc2UiOnsiQHR5cGUiOiJ0eXBlLmdvb2dsZWFwaXMuY29tL29wZXJhdGlvbiIsImlkIjoiNjQ0ODA0MTc0MDQ1NzE0MzMxNSIsImluc2VydFRpbWUiOiIyMDIyLTA1LTEwVDIzOjA5OjAwLjc4Ny0wNzowMCIsIm5hbWUiOiJvcGVyYXRpb24tMTY1MjI0OTM0MDQzNi01ZGViNjQ3MDQ2MTMyLWFjMzExN2VhLTA3OGZmMzMzIiwib3BlcmF0aW9uVHlwZSI6InN0b3AiLCJwcm9ncmVzcyI6IjAiLCJzZWxmTGluayI6Imh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL2NvbXB1dGUvdjEvcHJvamVjdHMvc3BvdG9uLXByb2plY3Qvem9uZXMvdXMtd2VzdDEtYi9vcGVyYXRpb25zL29wZXJhdGlvbi0xNjUyMjQ5MzQwNDM2LTVkZWI2NDcwNDYxMzItYWMzMTE3ZWEtMDc4ZmYzMzMiLCJzZWxmTGlua1dpdGhJZCI6Imh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL2NvbXB1dGUvdjEvcHJvamVjdHMvc3BvdG9uLXByb2plY3Qvem9uZXMvdXMtd2VzdDEtYi9vcGVyYXRpb25zLzY0NDgwNDE3NDA0NTcxNDMzMTUiLCJzdGFydFRpbWUiOiIyMDIyLTA1LTEwVDIzOjA5OjAwLjgwMy0wNzowMCIsInN0YXR1cyI6IlJVTk5JTkciLCJ0YXJnZXRJZCI6Ijg0OTQ5Njg1Mzg5MjY3NjA0NjQiLCJ0YXJnZXRMaW5rIjoiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vY29tcHV0ZS92MS9wcm9qZWN0cy9zcG90b24tcHJvamVjdC96b25lcy91cy13ZXN0MS1iL2luc3RhbmNlcy95d3QtdGVzdC1pbnN0YW5jZTMiLCJ1c2VyIjoiemhhbmd5YW5ib0B5dW5pb24taGsuY29tIiwiem9uZSI6Imh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL2NvbXB1dGUvdjEvcHJvamVjdHMvc3BvdG9uLXByb2plY3Qvem9uZXMvdXMtd2VzdDEtYiJ9LCJzZXJ2aWNlTmFtZSI6ImNvbXB1dGUuZ29vZ2xlYXBpcy5jb20ifSwicmVjZWl2ZVRpbWVzdGFtcCI6IjIwMjItMDUtMTFUMDY6MDk6MDEuNDE3OTAwODA2WiIsInJlc291cmNlIjp7ImxhYmVscyI6eyJpbnN0YW5jZV9pZCI6Ijg0OTQ5Njg1Mzg5MjY3NjA0NjQiLCJwcm9qZWN0X2lkIjoic3BvdG9uLXByb2plY3QiLCJ6b25lIjoidXMtd2VzdDEtYiJ9LCJ0eXBlIjoiZ2NlX2luc3RhbmNlIn0sInNldmVyaXR5IjoiTk9USUNFIiwidGltZXN0YW1wIjoiMjAyMi0wNS0xMVQwNjowOTowMC41MjcxNDVaIn0='
}
```

### 测试
