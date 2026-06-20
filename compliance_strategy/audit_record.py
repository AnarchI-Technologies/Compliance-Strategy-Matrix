from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(frozen=True)
class RevenueEvent:
    customer_reference: str
    service_type: str
    amount_usd: float
    control_id: str = "IC-REV-001"


@dataclass(frozen=True)
class AuditRecord:
    audit_token: str
    timestamp: str
    classification: str
    customer_reference: str
    service_type: str
    amount_usd: float
    control_id: str
    review_status: str


def build_audit_record(event: RevenueEvent) -> AuditRecord:
    if not event.customer_reference.strip():
        raise ValueError("customer_reference is required")
    if not event.service_type.strip():
        raise ValueError("service_type is required")
    if event.amount_usd < 0:
        raise ValueError("amount_usd cannot be negative")

    return AuditRecord(
        audit_token=f"AUDIT-ANARCHI-{uuid4().hex[:10].upper()}",
        timestamp=datetime.now(timezone.utc).isoformat(),
        classification="PUBLIC_SAFE_SERVICE_REVENUE_EVENT",
        customer_reference=event.customer_reference.strip(),
        service_type=event.service_type.strip(),
        amount_usd=round(event.amount_usd, 2),
        control_id=event.control_id.strip() or "IC-REV-001",
        review_status="REQUIRES_ACCOUNTING_AND_COUNSEL_REVIEW",
    )

