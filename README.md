# Adobe Analytics MCP Local Example

Simple local Python example to connect and explore Adobe Analytics MCP using OAuth Server-to-Server authentication.

## Prerequisites

Before starting, make sure you have:

- Adobe Analytics access
- Adobe Analytics MCP access
- At least one Report Suite access
- Adobe Developer Console access
- Python 3.11 or later

If you want step-by-step setup instructions, please refer to the Medium article below:

https://medium.com/@dhamiabhishek3496/how-to-connect-adobe-analytics-mcp-server-locally-using-oauth-server-to-server-authentication-07ea25526d6f

---

# Setup

## 1. Clone Repository

```bash
git clone https://github.com/abhishekDhami/adobe-analytics-mcp-oAuth.git
```

Open project folder:

```bash
cd adobe-analytics-mcp-oAuth
```

---

## 2. Create Virtual Environment

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create `.env` file using `.env.example`.

```text
ACCESS_TOKEN=
CLIENT_ID=
ORG_ID=
```

These values can be copied from Adobe Developer Console OAuth Server-to-Server credentials page.

---

## 5. Run Application

```bash
python app.py
```

If everything is configured correctly, available Adobe Analytics MCP tools should be printed in terminal.

---

# What This Example Covers

This example focuses only on:

- Local Adobe Analytics MCP connectivity
- OAuth Server-to-Server authentication
- Listing available MCP tools
- Basic MCP validation

This project intentionally keeps the setup simple and beginner friendly for local MCP exploration.
