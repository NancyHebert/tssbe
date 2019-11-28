"""
 This little helper helps encode SQLAlchemy rows to JSON
 in a json.dumps statement. Otherwise, the row will not
 serialize if it contains a date or a decimal.

 Usually used in a resource.

 USE: resp.body = json.dumps([dict(row) for row in result], default=encoder)
"""
import decimal
import datetime


def encoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)
