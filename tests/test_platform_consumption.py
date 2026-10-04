from pathlib import Path
import unittest


class PlatformConsumptionContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = Path("platform-consumption/capability-consumption.yaml").read_text(encoding="utf-8")

    def test_canonical_api_and_kind(self):
        self.assertIn("apiVersion: platform.mayabank.example/v1alpha1", self.text)
        self.assertIn("kind: CapabilityConsumption", self.text)

    def test_shared_capabilities_are_declared(self):
        for capability in ("identity", "observability", "secrets", "gitops", "quality"):
            self.assertIn(f"  {capability}:\n    mode: CONSUME_SHARED", self.text)

    def test_non_hot_path_specialists_are_reference_only(self):
        for owner in (
            "TradeOps-GenAI-Integration",
            "mayabank-kafka-ddd-openshift",
            "mayabank-azure-cloud-ai-platform",
            "mayabank-api-management-architecture",
        ):
            self.assertIn(f"owner: {owner}", self.text)
        self.assertGreaterEqual(self.text.count("mode: REFERENCE_ONLY"), 7)

    def test_market_access_capabilities_remain_product_owned(self):
        for capability in (
            "market-access-hot-path",
            "fix-session-sequence-recovery",
            "deterministic-pre-trade-risk",
            "market-data-execution-path",
            "drop-copy-reconciliation",
            "latency-time-evidence",
        ):
            self.assertIn(f"- {capability}", self.text)

    def test_non_destructive_lifecycle(self):
        self.assertIn("adoptionPolicy: Observe", self.text)
        self.assertIn("deletionPolicy: Retain", self.text)

    def test_no_embedded_runtime_endpoint_or_credentials(self):
        forbidden = (
            "issuer:",
            "otlpEndpoint:",
            "password:",
            "clientSecret:",
            "accessToken:",
            "privateKey:",
        )
        for token in forbidden:
            self.assertNotIn(token, self.text)


if __name__ == "__main__":
    unittest.main()
