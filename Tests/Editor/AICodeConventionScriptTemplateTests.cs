using System.Reflection;
using NUnit.Framework;
using ReferenceBinding;
using UnityEditor;
using UnityEngine;

namespace ActionFit.AICodeConvention.Editor.Tests
{
    public sealed class AICodeConventionScriptTemplateTests
    {
        private const string TemplatePath =
            "Packages/com.actionfit.ai-codeconvention/Editor/ScriptTemplates/ActionFitConventionMonoBehaviour.cs.txt";

        [Test]
        public void TemplateAsset_IsLoadableAndUsesUnityScriptTokens()
        {
            var template = AssetDatabase.LoadAssetAtPath<TextAsset>(TemplatePath);

            Assert.That(template, Is.Not.Null);
            StringAssert.Contains("#SCRIPTNAME#", template.text);
            StringAssert.Contains("#ROOTNAMESPACEBEGIN#", template.text);
            StringAssert.Contains("#ROOTNAMESPACEEND#", template.text);
        }

        [Test]
        public void TemplateText_UsesRuntimeReadOnlyRoleContainers()
        {
            var template = AssetDatabase.LoadAssetAtPath<TextAsset>(TemplatePath);

            Assert.That(template, Is.Not.Null);
            StringAssert.Contains("public sealed class Refs", template.text);
            StringAssert.Contains("public sealed class Assets", template.text);
            StringAssert.Contains("public sealed class Settings", template.text);
            StringAssert.Contains("using ReferenceBinding;", template.text);
            StringAssert.Contains(
                "[SerializeField, RequiredChildReference(\"ContentRoot\")]",
                template.text);
            StringAssert.Contains("private Transform contentRoot;", template.text);
            StringAssert.Contains("[RequiredReference(\"ICON_SPRITE_MISSING\")]", template.text);
            StringAssert.Contains("private Sprite iconSprite;", template.text);
            StringAssert.Contains("[SerializeField] private float animationDurationSeconds", template.text);
            StringAssert.Contains("public Refs References => refs;", template.text);
            StringAssert.Contains("public Assets AssetReferences => assets;", template.text);
            StringAssert.Contains("public Settings Configuration => settings;", template.text);
            StringAssert.Contains("private void OnValidate()", template.text);
            StringAssert.Contains("ReferenceBindingRequests.Enqueue(this);", template.text);
            StringAssert.Contains(
                "#if UNITY_EDITOR\n" +
                "    private void OnValidate()\n" +
                "    {\n" +
                "        ReferenceBindingRequests.Enqueue(this);\n" +
                "    }\n" +
                "#endif",
                template.text);
            StringAssert.DoesNotContain(" set;", template.text);
            StringAssert.DoesNotContain("ReferenceBinding.Editor", template.text);
            StringAssert.DoesNotContain("void Start", template.text);
            StringAssert.DoesNotContain("void Update", template.text);
        }

        [Test]
        public void RenderedCompileProbe_IsAMonoBehaviour()
        {
            Assert.That(
                typeof(ActionFit.TemplateSmoke.GeneratedConventionProbe).IsSubclassOf(typeof(MonoBehaviour)),
                Is.True);
        }

        [Test]
        public void RenderedCompileProbe_UsesReferenceBindingContract()
        {
            FieldInfo field = typeof(ActionFit.TemplateSmoke.GeneratedConventionProbe.Refs)
                .GetField("contentRoot", BindingFlags.Instance | BindingFlags.NonPublic);

            Assert.That(field, Is.Not.Null);

            var requiredChild = field.GetCustomAttribute<RequiredChildReferenceAttribute>();

            Assert.That(requiredChild, Is.Not.Null);
            Assert.That(requiredChild.ObjectName, Is.EqualTo("ContentRoot"));
            Assert.That(field.GetCustomAttribute<RequiredReferenceAttribute>(), Is.Null);
            Assert.That(field.GetCustomAttribute<AutoWireChildAttribute>(), Is.Null);

            FieldInfo assetField = typeof(ActionFit.TemplateSmoke.GeneratedConventionProbe.Assets)
                .GetField("iconSprite", BindingFlags.Instance | BindingFlags.NonPublic);

            Assert.That(assetField, Is.Not.Null);
            Assert.That(
                assetField.GetCustomAttribute<RequiredReferenceAttribute>()?.ErrorCode,
                Is.EqualTo("ICON_SPRITE_MISSING"));
            Assert.That(assetField.GetCustomAttribute<AutoWireChildAttribute>(), Is.Null);
            Assert.That(
                typeof(ActionFit.TemplateSmoke.GeneratedConventionProbe).GetMethod(
                    "OnValidate",
                    BindingFlags.Instance | BindingFlags.NonPublic),
                Is.Not.Null);
        }
    }
}
