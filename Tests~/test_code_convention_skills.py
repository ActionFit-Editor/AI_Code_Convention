#!/usr/bin/env python3
"""Contract tests for AI Code Convention package guidance and skills."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = PACKAGE_ROOT / "Skills~"
SHARED_REFERENCE = SKILLS_ROOT / "Shared" / "references" / "unity-code-authoring-rules.md"
PROFILE_REFERENCE = (
    SKILLS_ROOT / "Shared" / "references" / "profiles" / "actionfit-unity.md"
)
OWNER_ROUTING_REFERENCE = SKILLS_ROOT / "Shared" / "references" / "owner-routing.md"
RETIREMENT_REFERENCE = (
    SKILLS_ROOT / "Shared" / "references" / "local-convention-retirement.md"
)
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
PROFILE_RULE_IDS = (
    "AFCC-PRO-001",
    "AFCC-PRO-002",
    "AFCC-STY-001",
    "AFCC-ORG-001",
    "AFCC-CMT-001",
    "AFCC-LOG-001",
    "AFCC-GRD-001",
    "AFCC-CPP-001",
    "AFCC-PRF-001",
    "AFCC-UTK-001",
    "AFCC-DUR-001",
    "AFCC-LOP-001",
    "AFCC-RFS-001",
    "AFCC-TWN-001",
    "AFCC-SER-003",
    "AFCC-UIF-001",
    "AFCC-RET-001",
)
CAT_ONLY_IDENTIFIERS = (
    "GameEvents",
    "Main.Loop",
    "TimeProvider",
    "DatabaseManager",
    "DataStore",
    "DataKeys",
    "UIViews",
    "IPopup",
    "ACTIONFIT_DEBUG",
    "StringTable",
    "GameString",
    "UI_",
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
        self.assertTrue(PROFILE_REFERENCE.is_file())
        self.assertTrue(OWNER_ROUTING_REFERENCE.is_file())
        self.assertTrue(RETIREMENT_REFERENCE.is_file())
        for agent in ("Codex", "Claude"):
            contents = self._read_skill(agent, "code-convention-help")
            self.assertIn("`PACKAGE_SKILLS.md`", contents)
            self.assertIn("references/unity-code-authoring-rules.md", contents)
            self.assertIn("references/profiles/actionfit-unity.md", contents)
            self.assertIn("references/owner-routing.md", contents)
            self.assertIn("references/local-convention-retirement.md", contents)
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
            self.assertIn("READY TO RETIRE", contents)
            self.assertIn("package-to-installed-skill drift", contents)
            self.assertIn("continue normally when local convention documents are absent", contents)

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
            self.assertIn("references/profiles/actionfit-unity.md", contents)
            self.assertIn("references/owner-routing.md", contents)
            self.assertIn("Continue normally when local convention documents are absent", contents)

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
        for rule_id in PROFILE_RULE_IDS:
            self.assertIn(rule_id, guide)
        self.assertIn("Design Input Provenance And Exclusions", guide)
        self.assertIn("did not match the installed owner package's public surface", guide)
        self.assertNotIn("AutoWireValidateAndSave", guide)
        self.assertNotIn("ReferenceProcessMode", guide)

    def test_package_is_guidance_only_and_uses_published_installer_dependency(self) -> None:
        manifest = json.loads((PACKAGE_ROOT / "package.json").read_text(encoding="utf-8"))
        self.assertEqual("0.2.0", manifest["version"])
        self.assertEqual(
            "1.1.84",
            manifest["dependencies"]["com.actionfit.custompackagemanager"],
        )
        self.assertFalse((PACKAGE_ROOT / "Runtime").exists())

    def test_stable_rule_headings_are_unique(self) -> None:
        guide = (PACKAGE_ROOT / "AI_GUIDE.md").read_text(encoding="utf-8")
        headings = re.findall(r"^### `(?P<rule>AFCC-[A-Z]+-[0-9]{3})`", guide, re.MULTILINE)

        self.assertEqual(len(headings), len(set(headings)))
        for rule_id in PROFILE_RULE_IDS:
            self.assertEqual(1, headings.count(rule_id))

    def test_profile_activation_is_explicit_and_defaults_to_portable_core(self) -> None:
        profile = PROFILE_REFERENCE.read_text(encoding="utf-8")
        guide = (PACKAGE_ROOT / "AI_GUIDE.md").read_text(encoding="utf-8")

        self.assertIn("Profile ID: `actionfit-unity`", profile)
        self.assertIn("Base profile: `portable-core`", profile)
        self.assertIn("AI Code Convention profile: actionfit-unity", profile)
        self.assertIn("Do not infer", profile)
        self.assertIn("`portable-core` is the default", guide)
        self.assertEqual("portable-core", self._resolve_profile("# Project\n"))
        self.assertEqual(
            "actionfit-unity",
            self._resolve_profile(
                "# Project\nAI Code Convention profile: actionfit-unity\n"
            ),
        )
        with self.assertRaises(ValueError):
            self._resolve_profile(
                "AI Code Convention profile: actionfit-unity\n"
                "AI Code Convention profile: actionfit-unity\n"
            )
        with self.assertRaises(ValueError):
            self._resolve_profile("AI Code Convention profile: inferred\n")

    def test_capability_gates_do_not_create_dependencies(self) -> None:
        profile = PROFILE_REFERENCE.read_text(encoding="utf-8")
        manifest = json.loads((PACKAGE_ROOT / "package.json").read_text(encoding="utf-8"))

        self.assertIn("Cysharp.Threading.Tasks", profile)
        self.assertIn("DG.Tweening", profile)
        self.assertIn("com.actionfit.sosingleton", profile)
        self.assertIn("do not install UniTask", profile)
        self.assertEqual(
            {"com.actionfit.custompackagemanager": "1.1.84"},
            manifest["dependencies"],
        )

    def test_owner_routes_use_installed_guides_without_inventing_apis(self) -> None:
        routing = OWNER_ROUTING_REFERENCE.read_text(encoding="utf-8")

        for package_id in (
            "com.actionfit.time",
            "com.actionfit.ui.foundation",
            "com.actionfit.referencebinding",
            "com.actionfit.sosingleton",
        ):
            self.assertIn(package_id, routing)
            self.assertIn(f"Packages/{package_id}/AI_GUIDE.md", routing)
        self.assertIn("Package/API Mismatch", routing)
        self.assertIn("Keep project-specific type names", routing)

    def test_retirement_contract_is_read_only_and_keeps_six_categories(self) -> None:
        retirement = RETIREMENT_REFERENCE.read_text(encoding="utf-8")

        self.assertIn("This is a read-only readiness contract", retirement)
        self.assertIn("READY TO RETIRE", retirement)
        self.assertIn("Local code-convention authority", retirement)
        self.assertIn("Package-to-installed-skill drift", retirement)
        self.assertIn("does not prove source-wide code compliance", retirement)
        self.assertIn("Do not add a seventh relationship category", retirement)

    def test_portable_and_profile_guidance_excludes_project_only_identifiers(self) -> None:
        normative_sources = (
            PACKAGE_ROOT / "AI_GUIDE.md",
            SHARED_REFERENCE,
            PROFILE_REFERENCE,
        )
        combined = "\n".join(path.read_text(encoding="utf-8") for path in normative_sources)

        for identifier in CAT_ONLY_IDENTIFIERS:
            self.assertNotIn(identifier, combined)

    def test_readme_and_guide_use_the_release_candidate_repository(self) -> None:
        readme = (PACKAGE_ROOT / "README.md").read_text(encoding="utf-8")
        guide = (PACKAGE_ROOT / "AI_GUIDE.md").read_text(encoding="utf-8")

        repository = "https://github.com/ActionFitGames/AI_Code_Convention.git"
        self.assertIn(f"{repository}#0.2.0", readme)
        self.assertIn(repository, guide)
        self.assertIn("Current package version at generation time: `0.2.0`", guide)

    def test_shell_wrapper_runs_the_python_contract_suite(self) -> None:
        script = PACKAGE_ROOT / "Tests" / "Shell" / "run-tests.sh"

        self.assertTrue(script.is_file())
        contents = script.read_text(encoding="utf-8")
        self.assertIn("Tests~/test_code_convention_skills.py", contents)

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

    @staticmethod
    def _resolve_profile(router_text: str) -> str:
        prefix = "AI Code Convention profile:"
        selectors = [
            line.strip()[len(prefix) :].strip()
            for line in router_text.splitlines()
            if line.strip().startswith(prefix)
        ]
        if not selectors:
            return "portable-core"
        if len(selectors) != 1 or selectors[0] != "actionfit-unity":
            raise ValueError("invalid profile selector")
        return selectors[0]


if __name__ == "__main__":
    unittest.main()
