# Close the mailbox and logout from the Gmail account
import imaplib
import email

# IMAP settings
imap_host = 'imap.gmail.com'
imap_user = 'my_email@gmail.com'
imap_pass = 'my_password'

# Connect to the Gmail server
imap = imaplib.IMAP4_SSL(imap_host)

# Login to the Gmail account
imap.login(imap_user, imap_pass)

# Select the mailbox you want to search for emails
imap.select('INBOX')

keyword1 = 'Asus'
keyword2 = 'StockX'

# Search for emails containing the specified keywords
# ... (previous code)

# Search for all emails in the INBOX
status, email_ids = imap.search(None, 'ALL')

# Loop through the list of email IDs returned by the search method
for email_id in email_ids[0].split():
    # Fetch the email
    status, email_data = imap.fetch(email_id, '(RFC822)')
    email_message = email.message_from_bytes(email_data[0][1])

    # Get the sender's name
    sender_name, sender_email = email.utils.parseaddr(email_message.get('From', ''))

    # Check if the sender's name contains the specified keywords
    if keyword1.lower() in sender_name.lower() or keyword2.lower() in sender_name.lower():
        # Delete the email
        imap.store(email_id, '+FLAGS', '\\Deleted')

# Expunge the marked emails (actually delete them)
imap.expunge()

# Close the mailbox and logout from the Gmail account
imap.close()
imap.logout()


