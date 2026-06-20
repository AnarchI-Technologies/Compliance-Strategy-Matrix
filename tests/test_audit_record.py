import unittest

from compliance_strategy import RevenueEvent, build_audit_record


class AuditRecordTests(unittest.TestCase):
    def test_builds_public_safe_audit_record(self):
        record = build_audit_record(RevenueEvent("customer-1", "software license", 1250.555))

        self.assertTrue(record.audit_token.startswith("AUDIT-ANARCHI-"))
        self.assertEqual(record.amount_usd, 1250.56)
        self.assertEqual(record.review_status, "REQUIRES_ACCOUNTING_AND_COUNSEL_REVIEW")

    def test_rejects_negative_amounts(self):
        with self.assertRaises(ValueError):
            build_audit_record(RevenueEvent("customer-1", "software license", -1))

    def test_requires_customer_reference(self):
        with self.assertRaises(ValueError):
            build_audit_record(RevenueEvent(" ", "software license", 100))


if __name__ == "__main__":
    unittest.main()

