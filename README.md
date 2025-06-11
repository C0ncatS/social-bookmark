# 📌 Social Bookmark

Welcome to **Social Bookmark**, a unique social web app that lets you bookmark and share your favorite images from anywhere on the internet! With our handy JavaScript bookmarklet, simply pin the tool to your browser, grab images from any site, and share them with a community that loves discovering and engaging with cool visuals. 🚀

---

## ✨ Features

- 🔖 **Bookmarklet Tool:** Pin our JavaScript tool to your bookmarks bar. Click it on any website to instantly collect and select images for sharing.
- 👍 **Social Interactions:** Like images, follow other users, and explore the latest posts from the community.
- 📰 **Dashboard:** Stay in the loop with a real-time feed of the latest activities and image posts.
- 🔐 **Authentication:** Secure sign-in and sign-up, including Google OAuth support.
- ⚡ **Redis Integration:** Fast and efficient tracking of image views.
- 🔑 **Password Reset:** SMTP is used to send password reset emails if you ever forget your password.
- 🛠️ **Built with Django:** Reliable and scalable backend.
- 🎨 **Frontend:** Responsive UI built with Django Templates.

---

## 🛣️ How It Works

### User Flow

1. 📝 **Sign Up / Sign In:**  
   Register a new account or log in with Google.

2. 📌 **Pin the Bookmark Tool:**  
   Drag our bookmarklet from the dashboard to your browser's bookmarks bar.

3. 🌐 **Browse Any Website:**  
   While surfing, click the Social Bookmark tool in your bookmarks.

4. 🖼️ **Pick Your Image:**  
   Instantly see all images on the page and select one to bookmark.

5. 🏷️ **Add Details:**  
   Give your image a catchy title and an optional description.

6. 🚩 **Post the Image:**  
   Share it with the community!

7. 🔍 **Explore & Engage:**  
   Browse, like, follow, and keep up with the live dashboard.

---

## 🛠️ Tech Stack

- **Backend:** Django
- **Authentication:** Google OAuth & standard login/signup
- **Image View Tracking:** Redis
- **Password Reset Emails:** SMTP
- **Frontend:** Django Templates

---

## ⚡ Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/C0ncatS/social-bookmark.git
   cd social-bookmark
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file in the project root and fill in your credentials:**

   ```env
   EMAIL_HOST_USER=your_smtp_username
   EMAIL_HOST_PASSWORD=your_smtp_password
   DEFAULT_FROM_EMAIL=your_email@example.com
   GOOGLE_OAUTH2_KEY=your_google_oauth_client_id
   GOOGLE_OAUTH2_SECRET=your_google_oauth_client_secret
   ```

4. **Install and run Redis:**  
   Redis is required for tracking image views.  
   You can find installation instructions for your operating system here:  
   👉 [Redis Installation Guide](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/)

5. **Configure Redis connection settings in your Django settings as needed.**

6. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Start the server:**
   ```bash
   python manage.py runserver
   ```

8. **Open in browser:**  
   Go to [http://localhost:8000](http://localhost:8000)

---

## 💡 Usage Tips

- **Pin the Bookmark Tool:**  
  After login, find the “Bookmark Tool” in your dashboard and drag it to your bookmarks bar.

- **Bookmark an Image:**  
  Click the bookmarklet on any website, select your image, and add details.

- **Socialize:**  
  Browse, like, follow, and use the dashboard for updates!

---

## 🤝 Contributing

We love contributions! Open issues or submit pull requests to help improve Social Bookmark.

---

### 🌟 Social Bookmark – Effortlessly save and share your favorite images from anywhere on the web!