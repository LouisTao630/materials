[TOC]

# Basic access authentication （BA）
BA认证方式需要在用户创建请求的时候提供用户名和密码。它不需要cookies、seesion定义、或者登陆页面。仅使用标准的HTTP Header字段，并且移除了握手连接。

## 服务器行为

当服务器端需要用户证明自身时，服务器需要对未认证的请求返回**HTTP401**状态，并且增加**WWW-Authenticate**头部字段告知访问的领域及用户名及密码的编码方式。

```
# 当前领域希望用utf-8编码返回用户名和密码
WWW-Authenticate: Basic realm="User Visible Realm" charset="UTF-8" 
```

## 客户端行为

当客户端需要发送一个认证的服务器端请求时，就需要使用Authorization字段来表示。

构造Authorization字段需要以下步骤：

1. 用户名和密码使用冒号连接。

2. 字符串需要编码成为八位序列。

3. 使用Base64的变种加密方式。

4. 添加Basic和一个空格在以上编码结果之前。

   ```
   Authorization: Basic QWxhZGRpbjpPcGVuU2VzYW1l
   ```
   
## 流程说明

```sequence
participant client
participant server
client -> server: /user/welcome(no auth)
server --> client: Status:401 WWW-Authentication: Basic realm="web site"
client -> server: /user/welcome(Authorization: Basic QWxhZGRpbjpPcGVuU2VzYW1l)
server --> client: Status: 200 OK
```

## 实现

1. 服务器端开启BA验证
2. 客户端访问资源（未提供认证信息)
3. 服务端返回401，并要求认证信息
4. 客户端再次访问（提供认证信息）

### Server
使用Spring boot 开启 spring security。
[代码地址]()
### Client
借助浏览器与抓包攻击

### 查看结果
![basic auth](images/basic_auth.png)
服务器端响应：
![basic auth server](images/basic_auth_2.png)
客户端响应：
![basic auth client](images/basic_auth_3.png)

## 参考资料
[wiki](https://en.wikipedia.org/wiki/Basic_access_authentication)
