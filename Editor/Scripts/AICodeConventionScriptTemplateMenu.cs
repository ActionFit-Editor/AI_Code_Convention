#if UNITY_EDITOR
using UnityEditor;

internal static class AICodeConventionScriptTemplateMenu
{
    private const string TemplatePath =
        "Packages/com.actionfit.ai-codeconvention/Editor/ScriptTemplates/ActionFitConventionMonoBehaviour.cs.txt";
    private const string DefaultFileName = "NewActionFitMonoBehaviour.cs";

    [MenuItem("Assets/Create/Scripting/ActionFit Convention MonoBehaviour Script", false, 81)]
    private static void CreateConventionMonoBehaviour()
    {
        ProjectWindowUtil.CreateScriptAssetFromTemplateFile(TemplatePath, DefaultFileName);
    }
}
#endif
