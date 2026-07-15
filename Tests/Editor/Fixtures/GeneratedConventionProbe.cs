using System;
using ReferenceBinding;
using UnityEngine;

namespace ActionFit.TemplateSmoke
{
public class GeneratedConventionProbe : MonoBehaviour
{
    #region Fields

    [SerializeField] private Refs refs = new();
    [SerializeField] private Assets assets = new();
    [SerializeField] private Settings settings = new();

    #endregion

    #region Properties

    public Refs References => refs;
    public Assets AssetReferences => assets;
    public Settings Configuration => settings;

    #endregion

    #region Unity Lifecycle

    private void OnValidate()
    {
#if UNITY_EDITOR
        ReferenceBindingRequests.Enqueue(this);
#endif
    }

    #endregion

    #region Serialized Types

    [Serializable]
    public sealed class Refs
    {
        [SerializeField]
        [RequiredReference("CONTENT_ROOT_MISSING")]
        [AutoWireChild("ContentRoot")]
        private Transform contentRoot;

        public Transform ContentRoot => contentRoot;
    }

    [Serializable]
    public sealed class Assets
    {
        [SerializeField]
        [RequiredReference("ICON_SPRITE_MISSING")]
        private Sprite iconSprite;

        public Sprite IconSprite => iconSprite;
    }

    [Serializable]
    public sealed class Settings
    {
        [SerializeField] private float animationDurationSeconds = 0.25f;

        public float AnimationDurationSeconds => animationDurationSeconds;
    }

    #endregion
}
}
