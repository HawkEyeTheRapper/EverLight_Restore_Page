---
layout: none
title: Memory Fragment
---

{% raw %}
# BoldGrid Backup on DH

**SYSTEM**: 

**USER**: Can you tell me how to use this boldgrid backup file on dreamhost utilizing the same domain 

**ASSISTANT**: 

**ASSISTANT**: To restore your BoldGrid backup file on DreamHost and use it with the same domain, follow these steps:

---

### **Step 1: Prepare Your Backup**
1. **Download the backup file** to your local machine if it's not already accessible.
2. **Unzip the backup file** to review its contents. It should typically include files such as:
   - Website files (e.g., `wp-content`, `wp-config.php`, etc.)
   - A database file (usually `.sql`).

---

### **Step 2: Prepare Your DreamHost Account**
1. **Log in to your DreamHost panel.**
2. Navigate to **Manage Websites** and confirm that your domain (e.g., `hawkeyetherapper.net`) is hosted.
3. If you have an existing WordPress installation, delete it or clear the directory. Ensure the directory for your domain (e.g., `/home/username/hawkeyetherapper.net`) is empty.

---

### **Step 3: Upload Your Backup Files**
1. Use an **FTP client** (e.g., FileZilla) or DreamHost's file manager to upload the extracted website files to the root directory of your domain (`hawkeyetherapper.net`).
   - If you have a `public_html` folder, upload the files there.
2. Make sure the **`wp-config.php`** file is updated with the correct database details (see below).

---

### **Step 4: Create and Import the Database**
1. Go to the **Databases** section in your DreamHost panel.
2. **Create a new MySQL database** for your website. Note down:
   - Database name
   - Database username and password
   - Hostname (e.g., `mysql.hawkeyetherapper.net`)
3. Use **phpMyAdmin** (accessible via the DreamHost panel) to **import the `.sql` file** from your backup.

---

### **Step 5: Update `wp-config.php`**
1. Edit the `wp-config.php` file in your uploaded files to match the new database credentials:
   ```php
   define('DB_NAME', 'your_database_name');
   define('DB_USER', 'your_database_username');
   define('DB_PASSWORD', 'your_database_password');
   define('DB_HOST', 'your_database_host');
   ```
2. Save the file and upload it back to your server if edited locally.

---

### **Step 6: Update DNS (if necessary)**
Ensure your domain is pointing to the DreamHost server. Update the DNS records if needed via DreamHost's DNS management or your domain registrar.

---

### **Step 7: Test Your Website**
1. Open your browser and go to `hawkeyetherapper.net`.
2. Verify that your website is working properly.

---

Let me know if you need help with any of these steps or specific troubleshooting!
{% endraw %}
