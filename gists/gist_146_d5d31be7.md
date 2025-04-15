---
layout: none
title: Memory Fragment
---

{% raw %}
# Restore BoldGrid Backup

**SYSTEM**: 

**USER**: Can you restore this site to my Wordpress for me? I used bold grid to create it but can’t figure out how to use it to restore the site. 

**ASSISTANT**: 

**ASSISTANT**: I can help guide you through restoring your WordPress site using the BoldGrid backup file you provided. Here are the steps to restore your website:

### **Step 1: Upload Backup File**
1. Log in to your WordPress admin dashboard.
2. Navigate to **BoldGrid Backup** under the WordPress menu.
3. Go to the **Restore or Manage Backups** section.
4. Click the **Upload Backup File** button and upload the `.zip` file you provided.

### **Step 2: Restore the Site**
1. Once the backup is uploaded, it should appear in the backup list.
2. Click on the **Restore** button next to the uploaded backup file.
3. Confirm the restoration process when prompted.

### **Step 3: Verify the Site**
- Once the restoration process is complete, visit your website to ensure everything has been restored correctly.
- Check for broken links, missing files, or theme discrepancies.

### **Alternative Option: Manual Restore**
If BoldGrid isn't working correctly, I can guide you through manually restoring the backup using cPanel or FTP. Let me know if you'd like to proceed with this approach.

**USER**: Yes please

**ASSISTANT**: Here are the steps to manually restore your WordPress site using cPanel or FTP:

---

### **Step 1: Extract the Backup File**
1. Extract the `.zip` file on your computer.
   - You should see folders like **wp-content**, **wp-admin**, and a **database file** (often ends in `.sql`).

---

### **Step 2: Upload Website Files**
1. **Log in to your cPanel or FTP client:**
   - Use your hosting credentials to log in.
2. **Navigate to your WordPress installation folder:**
   - Usually, it's located in `public_html` or a subdirectory like `www.hawkeyetherapper.net`.
3. **Upload the extracted files:**
   - Drag and drop the extracted folders (e.g., **wp-content**, **wp-admin**) and overwrite any existing files.

---

### **Step 3: Restore the Database**
1. **Log in to cPanel** and go to **phpMyAdmin**:
   - Alternatively, you can use a database management tool provided by your host.
2. **Backup the current database**:
   - Export the existing database as a precaution.
3. **Delete the existing database content**:
   - Open your WordPress database and delete all tables (optional, if you need a fresh restore).
4. **Import the backup database:**
   - Upload the `.sql` file included in your backup using the **Import** tab in phpMyAdmin.

---

### **Step 4: Update wp-config.php**
1. In the extracted files, locate the `wp-config.php` file.
2. Ensure the database credentials match your hosting setup:
   - **DB_NAME:** The name of the database you imported.
   - **DB_USER:** Your database username.
   - **DB_PASSWORD:** Your database password.
3. Upload the updated `wp-config.php` file to your server (overwrite if necessary).

---

### **Step 5: Verify and Test the Site**
1. Open your website in a browser to confirm it is working.
2. Log in to the WordPress admin dashboard to check for any missing plugins or theme files.
3. Test links, images, and other functionalities.

---

### **Need Direct Assistance?**
If you encounter errors or need help with specific steps (like identifying database credentials or handling conflicts), share details about the issue, and I’ll guide you further.
{% endraw %}
