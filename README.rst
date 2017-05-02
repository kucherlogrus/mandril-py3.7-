========
Mandrill
========

.. note::

   The upstream upstream version of mandrill-api-python appears maintained with
   reasonable PRs unmerged for over a year. This fork exists to merge such PRs
   until Mailchimp manage to get around to maintaining their own software.
   Help with code review really welcomed.

Mandrill is a Python API client and suite of CLI-based tools for the Mandrill
email as a platform service.

The API client is comprehensive, but the CLI functionality is minimal at this time.

* Examples::

      import mandrill

      client = mandrill.Mandrill('YOUR_API_KEY')
      print client.users.ping()

* CLI Examples::

      mandrill setup
      mandrill ping -c10
      mandrill send -f from@example.com -t to@example.com -s "My Subject Line" < content.html
