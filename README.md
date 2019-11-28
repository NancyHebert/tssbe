TSS (Thesis Supervisor Search)
==========================

This solution can be deployed in three environments: local development, staging (Shakespeare server), and prod.

Step 1:
=======
GIT

Step 2:
======

Development environment

. clean.sh; docker-compose -f docker-compose-dev.yml up -d

Note: the -d flag runs the process as a daemon. If you'd like to see log messages live, don't include that flag.

Staging/Prod environment

. clean.sh; docker-compose up -d
