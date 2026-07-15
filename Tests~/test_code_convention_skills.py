#!/usr/bin/env python3
"""Contract tests for AI Code Convention package guidance and skills."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = PACKAGE_ROOT / "Skills~"
SHARED_REFERENCE = SKILLS_ROOT / "Shared" / "references" / "unity-code-authoring-rules.md"
SKILL_NAMES = (
    "code-convention-help",
    "code-convention-check",
    "code-convention-apply",
)
CATEGORIES = (
    "Aligned",
    "Local Extension",
    "Conflict — Local Wins",
    "Package Default",
    "Local Only",
    "Package/API Mismatch",
)


class CodeConventionSkillTests(unittest.TestCase):
    def test_manifest_registers_schema_v2_contract_for_both_agents(self) -> None:
        manifest = json.loads((SKILLS_ROOT / "manifest.json").read_text(encoding="utf-8"))

        self.assertEqual(2, manifest["schemaVersion"])
        self.assertEqual("code-convention", manifest["skillPrefix"])
        self.assertEqual("code-convention-help", manifest["helpSkill"])
        self.assertEqual(
            [
                {
                    "name": "code-convention-help",
                    "agents": ["codex", "claude"],
                    "includeShared": True,
                    "access": "read-only",
                },
                {
                    "name": "code-convention-check",
                    "agents": ["codex", "claude"],
                    "includeShared": True,
                    "access": "read-only",
                },
                {
                    "name": "code-convention-apply",
                    "agents": ["codex", "claude"],
                    "includeShared": True,
                    "access": "write-capable",
                },
            ],
            manifest["skills"],
        )

    def test_help_uses_generated_inventory_and_shared_progressive_reference(self) -> None:
        self.assertTrue(SHARED_REFERENCE.is_file())
        for agent in ("Codex", "Claude"):
            contents = self._read_skill(agent, "code-convention-help")
            self.assertIn("`PACKAGE_SKILLS.md`", contents)
            self.assertIn("references/unity-code-authoring-rules.md", contents)
            self.assertIn("com.actionfit.referencebinding/AI_GUIDE.md", contents)

        authored_inventory = list(SKILLS_ROOT.rglob("PACKAGE_SKILLS.md"))
        self.assertEqual([], authored_inventory)

    def test_check_contract_uses_stable_categories_and_remains_read_only(self) -> None:
        for agent in ("Codex", "Claude"):
            contents = self._read_skill(agent, "code-convention-check")
            for category in CATEGORIES:
                self.assertIn(f"`{category}`", contents)
            for field in (
                "Package rule ID",
                "Local or owner source",
                "Effective rule",
                "Recommended follow-up",
            ):
                self.assertIn(f"`{field}`", contents)
            self.assertIn("git status --short --untracked-files=all", contents)
            self.assertIn("Keep the entire check read-only", contents)
            self.assertIn("not source-code compliance proof", contents)
            self.assertIn("`AFCC-REF-001`", contents)
            self.assertIn("intentionally excluded design-input specialization", contents)
            self.assertIn("Do not claim that the consuming project's local docs contain", contents)
            self.assertIn("package rule ID `N/A`", contents)

    def test_apply_requires_existing_authority_and_allows_guarded_implicit_selection(self) -> None:
        for agent in ("Codex", "Claude"):
            contents = self._read_skill(agent, "code-convention-apply")
            self.assertIn("does not create edit authority", contents)
            self.assertIn("authorized a concrete Unity code change and target scope", contents)
            self.assertIn("Implement only the authorized files and behavior", contents)
            self.assertIn("Request separate approval", contents)
            self.assertIn("Decision Log", contents)
            self.assertIn("does not own Jira", contents)
            self.assertIn("references/unity-code-authoring-rules.md", contents)

        metadata = (
            SKILLS_ROOT
            / "Codex"
            / "code-convention-apply"
            / "agents"
            / "openai.yaml"
        ).read_text(encoding="utf-8")
        self.assertIn("allow_implicit_invocation: true", metadata)
        self.assertNotIn(
            "disable-model-invocation",
            self._read_skill("Claude", "code-convention-apply"),
        )

    def test_codex_and_claude_instruction_sources_are_equivalent(self) -> None:
        for name in SKILL_NAMES:
            self.assertEqual(self._read_skill("Codex", name), self._read_skill("Claude", name))

    def test_root_guide_owns_stable_rules_and_referencebinding_exclusion(self) -> None:
        guide = (PACKAGE_ROOT / "AI_GUIDE.md").read_text(encoding="utf-8")
        for rule_id in (
            "AFCC-PRE-001",
            "AFCC-PRE-002",
            "AFCC-AUT-001",
            "AFCC-CHG-001",
            "AFCC-ADP-001",
            "AFCC-DEC-001",
            "AFCC-OWN-001",
            "AFCC-STA-001",
            "AFCC-TIM-001",
            "AFCC-COM-001",
            "AFCC-LIF-001",
            "AFCC-ASY-001",
            "AFCC-PER-001",
            "AFCC-ECO-001",
            "AFCC-AST-001",
            "AFCC-SER-001",
            "AFCC-SER-002",
            "AFCC-ASM-001",
            "AFCC-REF-001",
            "AFCC-VAL-001",
            "AFCC-REP-001",
        ):
            self.assertIn(rule_id, guide)

        for category in CATEGORIES:
            self.assertIn(f"`{category}`", guide)
        self.assertIn("Design Input Provenance And Exclusions", guide)
        self.assertIn("did not match the installed owner package's public surface", guide)
        self.assertNotIn("AutoWireValidateAndSave", guide)
        self.assertNotIn("ReferenceProcessMode", guide)

    def test_package_is_guidance_only_and_uses_published_installer_dependency(self) -> None:
        manifest = json.loads((PACKAGE_ROOT / "package.json").read_text(encoding="utf-8"))
        self.assertEqual("0.1.0", manifest["version"])
        self.assertEqual(
            "1.1.84",
            manifest["dependencies"]["com.actionfit.custompackagemanager"],
        )
        self.assertFalse((PACKAGE_ROOT / "Runtime").exists())

    def test_sources_have_no_todos_or_machine_specific_input_path(self) -> None:
        text_files = [
            path
            for path in PACKAGE_ROOT.rglob("*")
            if path.is_file()
            and path.suffix.lower() in {".md", ".json", ".yaml", ".cs", ".asmdef"}
        ]
        combined = "\n".join(path.read_text(encoding="utf-8") for path in text_files)

        self.assertNotIn("[TODO", combined)
        self.assertNotIn("/Users/", combined)
        self.assertNotIn("UnityArchitectureGuide", combined)

    @staticmethod
    def _read_skill(agent: str, name: str) -> str:
        return (SKILLS_ROOT / agent / name / "SKILL.md").read_text(encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
