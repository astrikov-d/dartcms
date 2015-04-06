__author__ = 'astrikovd'

from watson.backends import PostgresSearchBackend


class DartCMSPostgresSearchBackend:
    search_config = "pg_catalog.russian"
    requires_installation = False