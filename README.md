# AI Code Convention (com.actionfit.ai-codeconvention)

Codex와 Claude를 위한 재사용 가능한 Unity 코드 작성 가이드입니다. 재사용 가능한 core와 명시적으로 선택한 profile을 결합하고, 구체적인 API를 설치된 owner로 routing하며, 사용자가 승인한 코드 변경 범위 안에서만 유효한 규칙을 적용합니다. 필요한 ReferenceBinding 지원을 포함한 opt-in ActionFit MonoBehaviour starter template 하나도 제공합니다.

이 패키지는 **Public** 저장소에서 배포됩니다. Runtime 어셈블리, EventBus 구현, 게임플레이 프레임워크, analyzer, formatter 또는 범용 code generation framework는 포함하지 않습니다. Editor 전용 generator는 Unity 기본 Project 창 흐름을 통해 새로운 convention starter script 하나를 생성합니다. Public 공개 범위는 소스를 읽을 수 있게 할 뿐, 자격 증명을 포함하거나 저장소의 명시적 라이선스 범위를 넘는 권리를 부여하지 않습니다.

## 설치

```json
{
  "dependencies": {
    "com.actionfit.custompackagemanager": "https://github.com/ActionFit-Editor/Custom_Package_Manager.git#1.1.100",
    "com.actionfit.referencebinding": "https://github.com/ActionFit-Editor/ReferenceBinding.git#0.1.2",
    "com.actionfit.ai-codeconvention": "https://github.com/ActionFit-Editor/AI_Code_Convention.git#0.4.8"
  }
}
```

Custom Package Manager는 카탈로그에서 설치할 때 선언된 두 ActionFit 의존성을 해석합니다. Unity는 패키지의 semantic-version 의존성 항목에서 전이 Git URL을 해석하지 않으므로 Git UPM을 직접 사용하는 경우 위 세 개의 root manifest 항목을 모두 유지해야 합니다.

## Unity 메뉴

- Convention MonoBehaviour: `Assets > Create > Scripting > ActionFit Convention MonoBehaviour Script`
- README: `Tools > Package > AI Code Convention > README`
- 이 패키지가 나중에 설정 ScriptableObject를 소유하거나 bootstrap한다면 같은 패키지 root 아래에 `Setting SO`를 추가합니다.

Convention template은 예시 `Refs`, `Assets`, `Settings` container, private 직렬화 backing field와 getter 전용 접근을 가진 새 `MonoBehaviour`를 생성합니다. `Refs.contentRoot` 예시는 `RequiredReference`와 정확한 이름의 `AutoWireChild`를 함께 사용하고, `Assets.iconSprite` 예시는 hierarchy wiring 없이 `RequiredReference`를 사용합니다. 전체 `OnValidate` 선언은 Editor guard 안에서 owner를 `ReferenceBindingRequests` queue에 넣습니다. 선택한 대상, 이름 변경 상호작용, `#SCRIPTNAME#` 치환과 root namespace 확장은 Unity가 소유합니다.

`com.actionfit.referencebinding@0.1.2`는 필수 의존성입니다. owner Runtime 어셈블리가 auto-reference되므로 생성된 스크립트는 Unity predefined assembly에서 컴파일됩니다. 사용하는 custom asmdef는 `com.actionfit.referencebinding`을 명시적으로 참조해야 하며 generator는 프로젝트 asmdef를 변경하지 않습니다. 메뉴 실행은 profile을 선택하거나 기존 스크립트를 변경하거나 Scene/Prefab을 저장하거나 이후 편집의 준수를 증명하지 않습니다.

## AI 가이드

- 사용하는 프로젝트에서 이 패키지를 변경하거나 진단하기 전에 `AI_GUIDE.md`를 읽습니다.
- 기본 profile은 `portable-core`입니다. 사용하는 프로젝트의 primary router가 정확한 selector `AI Code Convention profile: actionfit-unity`로 opt-in할 수 있습니다.
- 저장소 이름, 조직, 설치된 의존성 또는 폴더 구조로 profile을 추론하지 않습니다.
- 프로젝트 로컬 안전 규칙과 사실 기반 아키텍처는 권한 있는 context이며, 설치된 패키지/API owner는 해당 구체적 surface의 사실 기준입니다.
- `actionfit-unity` profile은 Inspector 작성 입력을 `Refs`, `Assets`, `Settings`로 구분하고 getter 전용 API로 노출하며, 런타임 동안 저장 값과 참조 identity를 변경하지 않습니다.
- `actionfit-unity` profile은 구체적 소유권을 우선합니다. 증거가 있는 외부 계약, 교체 가능한 운영 구현, 플랫폼/runtime 변형 또는 구현 없는 불가피한 어셈블리 경계가 있을 때만 새 interface를 허용합니다. 기존 interface가 자동 마이그레이션 대상이 되지는 않습니다.
- `actionfit-unity` profile은 구체적 의존성 graph가 비순환 DAG인 트리 지향 소유권을 목표로 합니다. composition root가 응집력 있는 feature/service node를 조립하고, 재사용 node는 프로젝트 중립 패키지가 될 수 있으며, 증거가 있는 외부 기능만 composition root에서 프로젝트 adapter와 연결되는 좁은 port가 됩니다.
- root `AI_GUIDE.md`의 `## Package Identity` 안에 `AI Product Composition Root: <package-id>`와 `AI Refactor target: package-oriented-product`를 명시하면, `actionfit-unity` profile은 구체적인 제품 composition을 하나의 제품 소유 비재사용 패키지에 둘 수 있습니다. 이 marker는 제품 composition 목표만 선택하며 code convention profile이나 마이그레이션 권한을 선택하지 않습니다.
- 새로 만들거나 의도적으로 수정한 Scene 코드는 `MonoBehaviour`를 얇은 직렬화 binder로 유지하고, plain C# owner를 재사용 가능한 로직 경계로 사용하며, 비직렬화 animation helper는 binder에서 정확한 대상과 lifetime 입력을 받습니다.
- 각 경계가 응집력 있게 컴파일, 테스트, 버전 관리 및 발전할 수 있다면 Origin/Core, Unity Binding, UI Foundation Binding, DOTween Animation, SDK Adapter, Installer 같은 선택 연동 축을 inward-dependent Leaf 패키지로 만들 수 있습니다. 기본 installer는 모든 leaf를 직접 사용자에게 강제하지 않고 전체 구성을 선택할 수 있습니다.
- 목표는 점진적입니다. 패키지 수 증가, 엄격한 tree형 runtime 참조, 추측성 interface, dependency injection container 또는 프로젝트 전체 재구성은 목표가 아닙니다.
- 상세 아키텍처 및 검증 가이드는 관련 Agent Skill과 함께 점진적으로 설치됩니다.

선택한 패키지 profile은 유일한 code convention 기준이 될 수 있습니다. Router가 profile을 선택하고, 명시적으로 선언된 제품 패키지가 패키지 지향 composition 목표를 소유하며, 남은 아키텍처 문서가 사실 기반 프로젝트 mapping만 포함한다면 별도의 로컬 convention 문서가 필요하지 않습니다.

## Agent Skill 안내

Custom Package Manager `1.1.100` 이상은 변경되거나 충돌하는 target을 보존하면서 schema v2 skill을 프로젝트 로컬 agent 폴더에 설치합니다.

- `$code-convention-help`: 상태를 변경하지 않고 선택한 profile, 유효한 rule identifier, owner route, skill과 안전 경계를 설명합니다.
- `$code-convention-check`: 문서화된 계약을 비교하고 profile을 반영한 유효 규칙과 로컬 convention 은퇴 준비 상태를 보고하며 파일을 변경하지 않았음을 증명합니다.
- `$code-convention-apply`: 선택한 profile과 설치된 API owner를 해석한 뒤 사용자가 구체적인 Unity 코드 변경을 승인한 경우에만 유효 convention을 적용합니다.

비교 skill은 `Aligned`, `Local Extension`, `Conflict — Local Wins`, `Package Default`, `Local Only`, `Package/API Mismatch`를 보고합니다. 은퇴 준비 상태는 일곱 번째 관계 범주가 아니라 별도 결과입니다. 이 검사는 문서 수준 convention audit이며 소스 전체 준수 scanner가 아닙니다.

## 어셈블리

- **Editor** (`com.actionfit.ai-codeconvention.Editor`): Editor 전용 패키지 어셈블리입니다.

## 안전 경계

- 직렬화 참조 동작은 필수 `com.actionfit.referencebinding/AI_GUIDE.md`로 routing합니다. 이 패키지는 API를 복제하거나 에셋 쓰기 mode를 추가하지 않고 문서화된 public attribute와 owner queue를 사용합니다.
- 패키지 publish, 저장소 생성, 태그와 카탈로그 등록은 각각 별도의 수동 작업입니다.
- 이 패키지의 공개 배포는 승인되었습니다. 저장소 공개 범위와 관계없이 token, 자격 증명 및 private 설정을 패키지 콘텐츠에 포함하면 안 됩니다.
