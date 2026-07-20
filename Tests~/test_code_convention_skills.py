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
SCRIPT_TEMPLATE = (
    PACKAGE_ROOT
    / "Editor"
    / "ScriptTemplates"
    / "ActionFitConventionMonoBehaviour.cs.txt"
)
SCRIPT_TEMPLATE_MENU = (
    PACKAGE_ROOT / "Editor" / "Scripts" / "AICodeConventionScriptTemplateMenu.cs"
)
SCRIPT_TEMPLATE_COMPILE_PROBE = (
    PACKAGE_ROOT
    / "Tests"
    / "Editor"
    / "Fixtures"
    / "GeneratedConventionProbe.cs"
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
    "AFCC-TRE-001",
    "AFCC-PKG-001",
    "AFCC-PCR-001",
    "AFCC-PRT-001",
    "AFCC-BND-001",
    "AFCC-ANI-001",
    "AFCC-PKG-002",
    "AFCC-ORG-001",
    "AFCC-CMT-001",
    "AFCC-LOG-001",
    "AFCC-GRD-001",
    "AFCC-CPP-001",
    "AFCC-PRF-001",
    "AFCC-INT-001",
    "AFCC-UTK-001",
    "AFCC-DUR-001",
    "AFCC-LOP-001",
    "AFCC-RFS-001",
    "AFCC-RFS-002",
    "AFCC-SER-004",
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
PRODUCT_ROOT_MARKER = "AI Product Composition Root: <package-id>"
PRODUCT_TARGET_MARKER = "AI Refactor target: package-oriented-product"
EXPECTED_PACKAGE_VERSION = "0.4.9"
EXPECTED_DEPENDENCIES = {
    "com.actionfit.custompackagemanager": "1.1.106",
    "com.actionfit.referencebinding": "0.1.3",
}


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
            self.assertIn(
                "Assets > Create > Scripting > ActionFit Convention MonoBehaviour Script",
                contents,
            )
            self.assertIn("general-purpose code-generation framework", contents)

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
            self.assertIn("always resolve the required `com.actionfit.referencebinding` owner", contents)
            self.assertIn("missing owner route", contents)
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
            self.assertIn("resolve the required `com.actionfit.referencebinding/AI_GUIDE.md`", contents)
            self.assertIn("stop before authoring serialized-reference code", contents)
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

    def test_package_is_editor_only_and_uses_published_required_dependencies(self) -> None:
        manifest = json.loads((PACKAGE_ROOT / "package.json").read_text(encoding="utf-8"))
        self.assertEqual(EXPECTED_PACKAGE_VERSION, manifest["version"])
        self.assertEqual(EXPECTED_DEPENDENCIES, manifest["dependencies"])
        self.assertFalse((PACKAGE_ROOT / "Runtime").exists())
        self.assertTrue(SCRIPT_TEMPLATE.is_file())
        self.assertTrue(SCRIPT_TEMPLATE_MENU.is_file())

    def test_editor_script_generator_uses_native_flow_and_safe_starter(self) -> None:
        menu = SCRIPT_TEMPLATE_MENU.read_text(encoding="utf-8")
        template = SCRIPT_TEMPLATE.read_text(encoding="utf-8")
        compile_probe = SCRIPT_TEMPLATE_COMPILE_PROBE.read_text(encoding="utf-8")
        readme = (PACKAGE_ROOT / "README.md").read_text(encoding="utf-8")
        guide = (PACKAGE_ROOT / "AI_GUIDE.md").read_text(encoding="utf-8")

        menu_path = "Assets/Create/Scripting/ActionFit Convention MonoBehaviour Script"
        template_path = (
            "Packages/com.actionfit.ai-codeconvention/Editor/ScriptTemplates/"
            "ActionFitConventionMonoBehaviour.cs.txt"
        )
        self.assertIn(f'[MenuItem("{menu_path}"', menu)
        self.assertEqual(
            1,
            menu.count("ProjectWindowUtil.CreateScriptAssetFromTemplateFile"),
        )
        self.assertIn(f'"{template_path}"', menu)
        self.assertIn('"NewActionFitMonoBehaviour.cs"', menu)
        for custom_write_api in (
            "File.",
            "Directory.",
            "System.IO",
            "StreamWriter",
            "WriteAllText",
            "Delete(",
            "Move(",
            "Copy(",
            "AssetDatabase.",
        ):
            self.assertNotIn(custom_write_api, menu)

        for token in (
            "#SCRIPTNAME#",
            "#ROOTNAMESPACEBEGIN#",
            "#ROOTNAMESPACEEND#",
        ):
            self.assertEqual(1, template.count(token))
        for container in ("Refs", "Assets", "Settings"):
            self.assertIn(f"public sealed class {container}", template)
        for serialized_field in (
            "[SerializeField] private Refs refs = new();",
            "[SerializeField] private Assets assets = new();",
            "[SerializeField] private Settings settings = new();",
            "private Transform contentRoot;",
            "private Sprite iconSprite;",
            "[SerializeField] private float animationDurationSeconds = 0.25f;",
        ):
            self.assertIn(serialized_field, template)
        for getter in (
            "public Refs References => refs;",
            "public Assets AssetReferences => assets;",
            "public Settings Configuration => settings;",
            "public Transform ContentRoot => contentRoot;",
            "public Sprite IconSprite => iconSprite;",
            "public float AnimationDurationSeconds => animationDurationSeconds;",
        ):
            self.assertIn(getter, template)
        for reference_binding_contract in (
            "using ReferenceBinding;",
            '[RequiredReference("CONTENT_ROOT_MISSING")]',
            '[RequiredReference("ICON_SPRITE_MISSING")]',
            '[AutoWireChild("ContentRoot")]',
            "private void OnValidate()",
            "#if UNITY_EDITOR",
            "ReferenceBindingRequests.Enqueue(this);",
            "#endif",
        ):
            self.assertIn(reference_binding_contract, template)
        self.assertIn(
            "#if UNITY_EDITOR\n"
            "    private void OnValidate()\n"
            "    {\n"
            "        ReferenceBindingRequests.Enqueue(this);\n"
            "    }\n"
            "#endif",
            template,
        )
        self.assertEqual(2, template.count("RequiredReference"))
        self.assertEqual(1, template.count("AutoWireChild"))
        self.assertEqual(1, template.count("ReferenceBindingRequests.Enqueue(this)"))
        for excluded in (
            " set;",
            "ReferenceBinding.Editor",
            "void Start",
            "void Update",
            "Tooltip",
        ):
            self.assertNotIn(excluded, template)

        rendered = (
            template.replace("#SCRIPTNAME#", "GeneratedConventionProbe")
            .replace(
                "    #ROOTNAMESPACEBEGIN#",
                "namespace ActionFit.TemplateSmoke\n{",
            )
            .replace("#ROOTNAMESPACEEND#", "}")
        )
        self.assertEqual(rendered, compile_probe)

        test_asmdef = json.loads(
            (
                PACKAGE_ROOT
                / "Tests"
                / "Editor"
                / "com.actionfit.ai-codeconvention.Editor.Tests.asmdef"
            ).read_text(encoding="utf-8")
        )
        self.assertIn("com.actionfit.referencebinding", test_asmdef["references"])

        for docs in (readme, guide):
            self.assertIn(menu_path.replace("/", " > "), docs)
        self.assertIn("AFCC-PRO-001", readme)
        self.assertIn(
            f"com.actionfit.referencebinding@{EXPECTED_DEPENDENCIES['com.actionfit.referencebinding']}",
            readme,
        )
        self.assertIn("does not read or write the repository's profile selector", guide)
        self.assertIn("RequiredReference", guide)
        self.assertIn("AutoWireChild", guide)
        self.assertIn("Package updates never rewrite generated scripts", guide)

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

    def test_optional_capability_gates_do_not_create_unrelated_dependencies(self) -> None:
        profile = PROFILE_REFERENCE.read_text(encoding="utf-8")
        manifest = json.loads((PACKAGE_ROOT / "package.json").read_text(encoding="utf-8"))

        self.assertIn("Cysharp.Threading.Tasks", profile)
        self.assertIn("DG.Tweening", profile)
        self.assertIn("com.actionfit.sosingleton", profile)
        self.assertIn("do not install UniTask", profile)
        self.assertEqual(EXPECTED_DEPENDENCIES, manifest["dependencies"])

    def test_actionfit_serialized_inputs_are_role_split_and_runtime_read_only(self) -> None:
        guide = (PACKAGE_ROOT / "AI_GUIDE.md").read_text(encoding="utf-8")
        profile = PROFILE_REFERENCE.read_text(encoding="utf-8")

        deprecated_refs = guide.split("### `AFCC-RFS-001`", 1)[1].split(
            "### `AFCC-RFS-002`", 1
        )[0]
        self.assertIn("Deprecated", deprecated_refs)
        self.assertIn("`AFCC-RFS-002`", deprecated_refs)
        self.assertIn("`AFCC-SER-004`", deprecated_refs)
        for rule_id in ("AFCC-RFS-001", "AFCC-RFS-002", "AFCC-SER-004"):
            self.assertIn(rule_id, profile)
        self.assertIn("AFCC-RFS-002", guide)
        self.assertIn("AFCC-SER-004", guide)
        for container in ("`Refs`", "`Assets`", "`Settings`"):
            self.assertIn(container, guide)
            self.assertIn(container, profile)
        self.assertIn("owner GameObject or any descendant", guide)
        self.assertIn("private `[SerializeField]` backing fields", guide)
        self.assertIn("getter-only", guide)
        self.assertIn("Do not expose setters or mutation methods", guide)
        self.assertIn("separately owned runtime model", guide)
        self.assertIn("never `AutoWireChild`", profile)
        self.assertIn("does not search the AssetDatabase", profile)

        for agent in ("Codex", "Claude"):
            apply_skill = self._read_skill(agent, "code-convention-apply")
            self.assertIn("`AFCC-RFS-002`", apply_skill)
            self.assertIn("`AFCC-SER-004`", apply_skill)
            self.assertIn("getter-only access", apply_skill)
            self.assertIn("separate runtime model", apply_skill)

    def test_actionfit_interfaces_require_evidenced_production_contracts(self) -> None:
        guide = (PACKAGE_ROOT / "AI_GUIDE.md").read_text(encoding="utf-8")
        profile = PROFILE_REFERENCE.read_text(encoding="utf-8")
        readme = (PACKAGE_ROOT / "README.md").read_text(encoding="utf-8")

        rule = guide.split("### `AFCC-INT-001`", 1)[1].split("### `AFCC-", 1)[0]
        self.assertIn("`AFCC-COM-001`", rule)
        self.assertIn("two or more active production implementations", rule)
        self.assertIn("Unit-test substitution alone is insufficient", rule)
        self.assertIn("Existing interfaces are not automatic migration targets", rule)
        self.assertIn("Do not mechanically replace an interface with an abstract class", rule)
        self.assertIn("one implementation", profile)
        self.assertIn("service locator", profile)
        self.assertIn("separate authority", profile)
        self.assertIn("AFCC-INT-001", readme)

    def test_actionfit_target_is_tree_oriented_package_neutral_and_port_guarded(self) -> None:
        guide = (PACKAGE_ROOT / "AI_GUIDE.md").read_text(encoding="utf-8")
        profile = PROFILE_REFERENCE.read_text(encoding="utf-8")
        shared = SHARED_REFERENCE.read_text(encoding="utf-8")
        readme = (PACKAGE_ROOT / "README.md").read_text(encoding="utf-8")
        combined = "\n".join((guide, profile, shared, readme))

        for rule_id in (
            "AFCC-TRE-001",
            "AFCC-PKG-001",
            "AFCC-PCR-001",
            "AFCC-PRT-001",
            "AFCC-BND-001",
            "AFCC-ANI-001",
            "AFCC-PKG-002",
        ):
            self.assertIn(rule_id, guide)
            self.assertIn(rule_id, profile)
        for phrase in (
            "tree-oriented",
            "directed acyclic",
            "composition root",
            "project-neutral",
            "concrete SDK",
            "narrow",
            "project adapters",
            "package count",
            "service locator",
            "whole-project remodeling",
        ):
            self.assertIn(phrase, combined)
        self.assertIn("one hypothetical implementation", combined)
        self.assertIn("does not inventory or judge every source file", guide)

        for agent in ("Codex", "Claude"):
            help_skill = self._read_skill(agent, "code-convention-help")
            check_skill = self._read_skill(agent, "code-convention-check")
            apply_skill = self._read_skill(agent, "code-convention-apply")
            self.assertIn("`$refactor-plan`", help_skill)
            self.assertIn("Do not infer source violations", check_skill)
            self.assertIn("Do not treat an AI Refactor proposal as edit authority", apply_skill)

    def test_product_composition_root_is_explicit_package_owned_and_profile_neutral(self) -> None:
        guide = (PACKAGE_ROOT / "AI_GUIDE.md").read_text(encoding="utf-8")
        profile = PROFILE_REFERENCE.read_text(encoding="utf-8")
        shared = SHARED_REFERENCE.read_text(encoding="utf-8")
        retirement = RETIREMENT_REFERENCE.read_text(encoding="utf-8")
        readme = (PACKAGE_ROOT / "README.md").read_text(encoding="utf-8")
        combined = "\n".join((guide, profile, shared, readme))

        for rule_id in ("AFCC-PCR-001", "AFCC-PRO-001", "AFCC-PKG-001"):
            self.assertIn(rule_id, guide)
        for marker in (PRODUCT_ROOT_MARKER, PRODUCT_TARGET_MARKER):
            self.assertIn(marker, guide)
            self.assertIn(marker, profile)
            self.assertIn(marker, shared)
            self.assertIn(marker, readme)
        for phrase in (
            "product-owned, non-reusable package",
            "complete trimmed",
            "`## Package Identity`",
            "sibling `package.json` `name`",
            "does not select `actionfit-unity`",
            "Absence of both markers retains the generic architecture target",
            "exactly one product package",
            "creates no authority",
        ):
            self.assertIn(phrase, guide)
        package_identity = guide.split("## Package Identity", 1)[1].split("##", 1)[0]
        for marker_prefix in (
            "AI Product Composition Root:",
            "AI Refactor target:",
        ):
            self.assertFalse(
                any(
                    line.strip().startswith(marker_prefix)
                    for line in package_identity.splitlines()
                )
            )
        self.assertNotIn("com.actionfit.cat.app", combined)
        self.assertIn("routing metadata", retirement)
        self.assertIn("duplicated marker in project documentation", retirement)

        marker_only_router = (
            "# Project\n"
            "AI Product Composition Root: com.example.product.app\n"
            "AI Refactor target: package-oriented-product\n"
        )
        self.assertEqual("portable-core", self._resolve_profile(marker_only_router))
        self.assertEqual(
            "actionfit-unity",
            self._resolve_profile(
                marker_only_router
                + "AI Code Convention profile: actionfit-unity\n"
            ),
        )

        for agent in ("Codex", "Claude"):
            help_skill = self._read_skill(agent, "code-convention-help")
            check_skill = self._read_skill(agent, "code-convention-check")
            apply_skill = self._read_skill(agent, "code-convention-apply")
            for contents in (help_skill, check_skill, apply_skill):
                self.assertIn("`AFCC-PCR-001`", contents)
            for marker in (PRODUCT_ROOT_MARKER, PRODUCT_TARGET_MARKER):
                self.assertIn(marker, help_skill)
                self.assertIn(marker, check_skill)
            self.assertIn("does not select `actionfit-unity`", help_skill)
            self.assertIn("route that scope to `$refactor-plan`", check_skill)
            self.assertIn("never duplicate it in project documentation", apply_skill)

    def test_actionfit_binder_animation_and_leaf_rules_are_explicit(self) -> None:
        guide = (PACKAGE_ROOT / "AI_GUIDE.md").read_text(encoding="utf-8")
        profile = PROFILE_REFERENCE.read_text(encoding="utf-8")
        shared = SHARED_REFERENCE.read_text(encoding="utf-8")
        combined = "\n".join((guide, profile, shared))

        for phrase in (
            "thin serialized binders",
            "sole serialization owner",
            "plain C#",
            "exact targets",
            "Origin/Core",
            "UI Foundation Binding",
            "DOTween Animation",
            "one package per class",
            "default installer",
        ):
            self.assertIn(phrase, combined)

        cpp_rule = guide.split("### `AFCC-CPP-001`", 1)[1].split("### `AFCC-", 1)[0]
        self.assertIn("complete declaration", cpp_rule)
        self.assertIn("`OnValidate`", cpp_rule)
        self.assertIn("#if UNITY_EDITOR", cpp_rule)

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
        manifest = json.loads((PACKAGE_ROOT / "package.json").read_text(encoding="utf-8"))
        readme = (PACKAGE_ROOT / "README.md").read_text(encoding="utf-8")
        guide = (PACKAGE_ROOT / "AI_GUIDE.md").read_text(encoding="utf-8")
        package_info = (
            PACKAGE_ROOT
            / "Editor"
            / "PackageInfo"
            / "ActionFitPackageInfo_SO.asset"
        ).read_text(encoding="utf-8")

        repository = "https://github.com/ActionFit-Editor/AI_Code_Convention.git"
        version = manifest["version"]
        self.assertEqual(EXPECTED_PACKAGE_VERSION, version)
        self.assertIn(f"{repository}#{version}", readme)
        self.assertIn(repository, guide)
        self.assertIn(f"Current package version at generation time: `{version}`", guide)
        self.assertIn(f"This `{version}` candidate", guide)
        self.assertIn("_repositoryVisibility: 0", package_info)
        for package_id, dependency_version in EXPECTED_DEPENDENCIES.items():
            self.assertIn(f"{package_id}@{dependency_version}", package_info)
        self.assertNotIn("`0.3.0`", package_info)

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
            and path.suffix.lower()
            in {".md", ".json", ".yaml", ".cs", ".asmdef", ".txt"}
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
