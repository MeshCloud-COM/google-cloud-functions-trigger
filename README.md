# 说明文档


### Google Cloud Functions 设置
* Python version: 3.8
* requests version:  2.25.1
* Entry point：  triggered_pubsub 或者 triggered_http

### 环境变量 设置
* WEBHOOK_URL = "http://xxxx"
* PROM_USER = ""
* PROM_PASS = ""


### 触发方式 设置
* HTTP triggered_http
* Pub/Sub triggered_pubsub


### 注意事项 
如果使用triggered_http设置Authentication  Allow unauthenticated invocations


### 设置环境变量
<img width="1716" alt="image" src="https://user-images.githubusercontent.com/10955940/168217884-49110adb-8338-4f03-9e26-f430f645aba3.png">


## 示例 一 创建订阅 并push到 由Cloud Functions 创建的 webhook
### 创建Logs Router接收器
![image](https://user-images.githubusercontent.com/10955940/167327865-98a1d8a5-d697-46b6-ba13-a9740d245a79.png)
![image](https://user-images.githubusercontent.com/10955940/167327881-d3e90d4c-6505-4f1f-8152-e5957e6391c9.png)
![image](https://user-images.githubusercontent.com/10955940/167328077-02f09eac-c51b-450a-8ca7-336c6045ad6e.png)
![image](https://user-images.githubusercontent.com/10955940/167328096-1693b4b9-fd9c-45e6-b793-55806ebadea4.png)
![image](https://user-images.githubusercontent.com/10955940/167328110-fcc2e30b-cd17-497a-a272-50f6eef1ee4b.png)
![image](https://user-images.githubusercontent.com/10955940/167328152-04202da8-1ff3-4f28-8ec0-e4878823a81e.png)
![image](https://user-images.githubusercontent.com/10955940/167328180-45c3c75e-b9dd-45a4-99fd-1a943f0a6497.png)

### 创建订阅
![image](https://user-images.githubusercontent.com/10955940/167328637-36a53abc-40be-4ca1-95d1-323c4ac77dc2.png)
![image](https://user-images.githubusercontent.com/10955940/167328650-46980969-623d-4a41-a609-ae76d2a9cad0.png)


##  示例 二 订阅 Google Cloud Pub/Sub 并处理消息

### 创建Logs Router接收器
![image](https://user-images.githubusercontent.com/10955940/167819841-0e273a0b-9069-4417-83ac-c144e45bed3e.png)
![image](https://user-images.githubusercontent.com/10955940/167819905-f552c339-d36d-4e51-909a-fcb635d2ca78.png)
![image](https://user-images.githubusercontent.com/10955940/167819937-1f5e6928-cb84-4fe1-a810-d7391741bec4.png)
![image](https://user-images.githubusercontent.com/10955940/167819983-a4fb52d6-72a7-4e3a-a1f5-21b5fd981391.png)
![image](https://user-images.githubusercontent.com/10955940/167820055-7c09310d-f321-4604-bfd9-02cb64423b09.png)
![image](https://user-images.githubusercontent.com/10955940/167820136-f4dc7956-5849-4e0c-b52a-09ab66b3fb7c.png)

### 创建订阅
<img width="1744" alt="image" src="https://user-images.githubusercontent.com/10955940/167820477-34ce85e6-0fef-4652-aed9-664d50f8775f.png">
<img width="1743" alt="image" src="https://user-images.githubusercontent.com/10955940/167820823-d68605d0-59ec-4e9f-bf57-fa2c014df4af.png">

### 消息体
```json
{'@type': 'type.googleapis.com/google.pubsub.v1.PubsubMessage', 'attributes': {'logging.googleapis.com/timestamp': '2022-05-11T06:09:00.527145Z'}, 'data': 'eyJpbnNlcnRJZCI6Ii15NDRlemplNnk3aXciLCJsb2dOYW1lIjoicHJvamVjdHMvc3BvdG9uLXByb2plY3QvbG9ncy9jbG91ZGF1ZGl0Lmdvb2dsZWFwaXMuY29tJTJGYWN0aXZpdHkiLCJvcGVyYXRpb24iOnsiZmlyc3QiOnRydWUsImlkIjoib3BlcmF0aW9uLTE2NTIyNDkzNDA0MzYtNWRlYjY0NzA0NjEzMi1hYzMxMTdlYS0wNzhmZjMzMyIsInByb2R1Y2VyIjoiY29tcHV0ZS5nb29nbGVhcGlzLmNvbSJ9LCJwcm90b1BheWxvYWQiOnsiQHR5cGUiOiJ0eXBlLmdvb2dsZWFwaXMuY29tL2dvb2dsZS5jbG91ZC5hdWRpdC5BdWRpdExvZyIsImF1dGhlbnRpY2F0aW9uSW5mbyI6eyJwcmluY2lwYWxFbWFpbCI6InpoYW5neWFuYm9AeXVuaW9uLWhrLmNvbSJ9LCJhdXRob3JpemF0aW9uSW5mbyI6W3siZ3JhbnRlZCI6dHJ1ZSwicGVybWlzc2lvbiI6ImNvbXB1dGUuaW5zdGFuY2VzLnN0b3AiLCJyZXNvdXJjZUF0dHJpYnV0ZXMiOnsibmFtZSI6InByb2plY3RzL3Nwb3Rvbi1wcm9qZWN0L3pvbmVzL3VzLXdlc3QxLWIvaW5zdGFuY2VzL3l3dC10ZXN0LWluc3RhbmNlMyIsInNlcnZpY2UiOiJjb21wdXRlIiwidHlwZSI6ImNvbXB1dGUuaW5zdGFuY2VzIn19XSwibWV0aG9kTmFtZSI6InYxLmNvbXB1dGUuaW5zdGFuY2VzLnN0b3AiLCJyZXF1ZXN0Ijp7IkB0eXBlIjoidHlwZS5nb29nbGVhcGlzLmNvbS9jb21wdXRlLmluc3RhbmNlcy5zdG9wIn0sInJlcXVlc3RNZXRhZGF0YSI6eyJjYWxsZXJJcCI6IjE2Ny4xNzkuNjguMjMiLCJjYWxsZXJTdXBwbGllZFVzZXJBZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDEuMC40OTUxLjQxIFNhZmFyaS81MzcuMzYsZ3ppcChnZmUpLGd6aXAoZ2ZlKSIsImRlc3RpbmF0aW9uQXR0cmlidXRlcyI6e30sInJlcXVlc3RBdHRyaWJ1dGVzIjp7ImF1dGgiOnt9LCJyZWFzb24iOiI4dVN5d0FZUUdnNURiMnhwYzJWMWJTQkdiRzkzY3ciLCJ0aW1lIjoiMjAyMi0wNS0xMVQwNjowOTowMC44Mzc1NjVaIn19LCJyZXNvdXJjZUxvY2F0aW9uIjp7ImN1cnJlbnRMb2NhdGlvbnMiOlsidXMtd2VzdDEtYiJdfSwicmVzb3VyY2VOYW1lIjoicHJvamVjdHMvc3BvdG9uLXByb2plY3Qvem9uZXMvdXMtd2VzdDEtYi9pbnN0YW5jZXMveXd0LXRlc3QtaW5zdGFuY2UzIiwicmVzcG9uc2UiOnsiQHR5cGUiOiJ0eXBlLmdvb2dsZWFwaXMuY29tL29wZXJhdGlvbiIsImlkIjoiNjQ0ODA0MTc0MDQ1NzE0MzMxNSIsImluc2VydFRpbWUiOiIyMDIyLTA1LTEwVDIzOjA5OjAwLjc4Ny0wNzowMCIsIm5hbWUiOiJvcGVyYXRpb24tMTY1MjI0OTM0MDQzNi01ZGViNjQ3MDQ2MTMyLWFjMzExN2VhLTA3OGZmMzMzIiwib3BlcmF0aW9uVHlwZSI6InN0b3AiLCJwcm9ncmVzcyI6IjAiLCJzZWxmTGluayI6Imh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL2NvbXB1dGUvdjEvcHJvamVjdHMvc3BvdG9uLXByb2plY3Qvem9uZXMvdXMtd2VzdDEtYi9vcGVyYXRpb25zL29wZXJhdGlvbi0xNjUyMjQ5MzQwNDM2LTVkZWI2NDcwNDYxMzItYWMzMTE3ZWEtMDc4ZmYzMzMiLCJzZWxmTGlua1dpdGhJZCI6Imh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL2NvbXB1dGUvdjEvcHJvamVjdHMvc3BvdG9uLXByb2plY3Qvem9uZXMvdXMtd2VzdDEtYi9vcGVyYXRpb25zLzY0NDgwNDE3NDA0NTcxNDMzMTUiLCJzdGFydFRpbWUiOiIyMDIyLTA1LTEwVDIzOjA5OjAwLjgwMy0wNzowMCIsInN0YXR1cyI6IlJVTk5JTkciLCJ0YXJnZXRJZCI6Ijg0OTQ5Njg1Mzg5MjY3NjA0NjQiLCJ0YXJnZXRMaW5rIjoiaHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vY29tcHV0ZS92MS9wcm9qZWN0cy9zcG90b24tcHJvamVjdC96b25lcy91cy13ZXN0MS1iL2luc3RhbmNlcy95d3QtdGVzdC1pbnN0YW5jZTMiLCJ1c2VyIjoiemhhbmd5YW5ib0B5dW5pb24taGsuY29tIiwiem9uZSI6Imh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL2NvbXB1dGUvdjEvcHJvamVjdHMvc3BvdG9uLXByb2plY3Qvem9uZXMvdXMtd2VzdDEtYiJ9LCJzZXJ2aWNlTmFtZSI6ImNvbXB1dGUuZ29vZ2xlYXBpcy5jb20ifSwicmVjZWl2ZVRpbWVzdGFtcCI6IjIwMjItMDUtMTFUMDY6MDk6MDEuNDE3OTAwODA2WiIsInJlc291cmNlIjp7ImxhYmVscyI6eyJpbnN0YW5jZV9pZCI6Ijg0OTQ5Njg1Mzg5MjY3NjA0NjQiLCJwcm9qZWN0X2lkIjoic3BvdG9uLXByb2plY3QiLCJ6b25lIjoidXMtd2VzdDEtYiJ9LCJ0eXBlIjoiZ2NlX2luc3RhbmNlIn0sInNldmVyaXR5IjoiTk9USUNFIiwidGltZXN0YW1wIjoiMjAyMi0wNS0xMVQwNjowOTowMC41MjcxNDVaIn0='}
```

### 测试
