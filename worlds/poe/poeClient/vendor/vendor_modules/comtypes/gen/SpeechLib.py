from enum import IntFlag

import comtypes.gen._C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_4 as __wrapper_module__
from comtypes.gen._C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_4 import (
    DISPID_SRGetPropertyString, STCInprocHandler, SPWF_INPUT,
    SpeechCategoryAudioOut, ISpResourceManager, SPSMF_SAPI_PROPERTIES,
    SPLO_DYNAMIC, DISPID_SDKSetBinaryValue, SAFT48kHz8BitStereo,
    SVEPhoneme, SPEVENT, SPPHRASE, UINT_PTR,
    SPINTERFERENCE_LATENCY_TRUNCATE_END, SVP_3, DISPID_SVEPhoneme,
    ISpProperties, SVP_17, DISPID_SRGCmdLoadFromObject,
    SpWaveFormatEx, SGSExclusive, DISPID_SOTs_NewEnum,
    DISPID_SOTGetAttribute, DISPID_SGRsCount,
    DISPID_SGRSTPropertyName, ISpRecoContext2, SPRECOGNIZERSTATUS,
    SPFM_NUM_MODES, SPCT_COMMAND, SP_VISEME_3, SLOStatic, ISpAudio,
    DISPID_SGRSAddRuleTransition, SVP_15, SP_VISEME_18, DISPID_SOTCId,
    SpeechAllElements, DISPID_SVAudioOutputStream,
    DISPID_SVSLastStreamNumberQueued, ISpeechGrammarRules,
    SPCT_SUB_DICTATION, eLEXTYPE_USER, SPPS_LMA,
    DISPID_SRCRetainedAudioFormat, DISPID_SVSInputWordLength,
    ISpEventSource, SAFTCCITT_ALaw_44kHzMono, DISPID_SVGetVoices,
    SVSFPurgeBeforeSpeak, SPSHT_EMAIL,
    DISPID_SRCEPropertyNumberChange, DISPID_SLWsItem,
    SpeechGrammarTagWildcard, eWORDTYPE_ADDED, SPSSuppressWord,
    DISPID_SVEStreamEnd, DISPID_SPRsItem, DISPID_SGRSTWeight,
    DISPID_SVPause, IInternetSecurityMgrSite, SDA_One_Trailing_Space,
    SPPS_Unknown, DISPID_SRGCmdLoadFromProprietaryGrammar,
    ISpeechObjectTokens, eLEXTYPE_PRIVATE18, eLEXTYPE_RESERVED4,
    DISPID_SGRsFindRule, SGRSTTDictation, ISpeechLexiconWord,
    ISpPhrase, DISPID_SRGRecoContext, DISPID_SWFEBitsPerSample,
    SAFTCCITT_uLaw_22kHzStereo, DISPID_SASCurrentSeekPosition,
    DISPID_SPIRule, SPSMF_UPS, DISPID_SRCState,
    DISPID_SAFGetWaveFormatEx, SVESentenceBoundary, DISPID_SLPsCount,
    ULONG_PTR, SDTDisplayText, DISPID_SPIReplacements,
    SPRECORESULTTIMES, DISPID_SVEEnginePrivate, ISpRecoCategory,
    DISPID_SRCBookmark, DISPID_SPEAudioSizeTime, DISPID_SGRSTsItem,
    DISPID_SGRSTPropertyValue, IStream, SPEI_TTS_AUDIO_LEVEL,
    DISPID_SPRuleEngineConfidence, SVEBookmark, DISPID_SRRAlternates,
    SPPS_Modifier, SpeechCategoryAppLexicons,
    SPWT_LEXICAL_NO_SPECIAL_CHARS, SPEI_SENTENCE_BOUNDARY, SGDisplay,
    DISPID_SRAllowAudioInputFormatChangesOnNextSet,
    DISPID_SPRDisplayAttributes, SAFTGSM610_22kHzMono,
    DISPID_SGRs_NewEnum, SPAS_CLOSED, SPFM_CREATE_ALWAYS,
    DISPID_SPPBRestorePhraseFromMemory, SPRS_ACTIVE, SSTTTextBuffer,
    SPEI_END_INPUT_STREAM, SPPHRASERULE, SREFalseRecognition,
    DISPID_SRGReset, ISpNotifySource, DISPID_SLWType, SPEI_VISEME,
    SASClosed, DISPID_SASetState, DISPID_SGRsCommitAndSave,
    DISPID_SGRSTsCount, eLEXTYPE_PRIVATE15, SPSVerb,
    ISpNotifyTranslator, DISPID_SPRuleNumberOfElements,
    SAFTADPCM_11kHzMono, DISPID_SRCRecognizer,
    DISPID_SPEDisplayAttributes, SPVPRI_NORMAL,
    DISPID_SPEEngineConfidence, SPDKL_DefaultLocation,
    DISPID_SRCERecognizerStateChange, IEnumSpObjectTokens,
    SPPS_RESERVED2, SREPropertyStringChange, ISpRecognizer3,
    ISpeechRecoResultTimes, DISPID_SPEAudioTimeOffset,
    SAFTGSM610_44kHzMono, SPCS_DISABLED, SpTextSelectionInformation,
    DISPID_SPARecoResult, DISPID_SPRNumberOfElements,
    SAFTADPCM_44kHzMono, ISpRecognizer, DISPID_SRGetPropertyNumber,
    ISpeechMMSysAudio, eLEXTYPE_PRIVATE14, ISpRecoResult,
    SPSHORTCUTPAIR, ISpObjectTokenCategory, SPPHRASEREPLACEMENT,
    DISPID_SPAsItem, SAFTADPCM_8kHzStereo, DISPID_SVGetProfiles,
    SVEPrivate, DISPID_SRRAudio, SVSFlagsAsync, SpeechMicTraining,
    Speech_Max_Pron_Length, DISPID_SLGenerationId, ISpPhraseAlt,
    DISPID_SRRTTickCount, SP_VISEME_6, eLEXTYPE_APP,
    SPEVENTSOURCEINFO, SPINTERFERENCE_LATENCY_WARNING,
    DISPID_SBSFormat, SRCS_Disabled,
    DISPID_SRCAudioInInterferenceStatus, SP_VISEME_2,
    ISpeechPhraseReplacements, SVSFParseSsml, SPEI_SOUND_START,
    SPCT_DICTATION, SVSFParseAutodetect,
    ISpeechTextSelectionInformation, SVSFNLPSpeakPunc,
    SAFT32kHz16BitMono,
    DISPID_SVAllowAudioOuputFormatChangesOnNextSet,
    _ISpeechRecoContextEvents, DISPID_SPERetainedStreamOffset,
    SPRS_ACTIVE_USER_DELIMITED, DISPID_SRSetPropertyNumber,
    SP_VISEME_9, DISPID_SPAStartElementInResult, SPPS_SuppressWord,
    SECFDefault, SWTDeleted, DISPID_SAVolume, STCInprocServer,
    DISPID_SFSOpen, ISpEventSink, DISPID_SRRSetTextFeedback,
    eLEXTYPE_PRIVATE7, DISPID_SVEVoiceChange,
    DISPID_SRGCmdLoadFromMemory, SpFileStream, SAFTADPCM_8kHzMono,
    eLEXTYPE_LETTERTOSOUND, DISPID_SOTGetStorageFileName,
    SAFT24kHz16BitStereo, SPEI_ADAPTATION, DISPID_SPRulesItem,
    SpeechGrammarTagDictation, DISPID_SRSClsidEngine, DISPID_SPRText,
    SRTExtendableParse, DISPID_SPPChildren, DISPID_SDKOpenKey,
    DISPID_SGRAddState, DISPID_SGRsItem, SVP_16,
    DISPID_SWFESamplesPerSec, DISPID_SPRulesCount,
    DISPID_SPRuleFirstElement, ISequentialStream, SPPS_RESERVED1,
    __MIDL___MIDL_itf_sapi_0000_0020_0002, DISPID_SPPConfidence,
    DISPID_SLRemovePronunciation, SPEI_PHRASE_START,
    DISPID_SGRSTs_NewEnum, SPRECOCONTEXTSTATUS, ISpeechPhraseInfo,
    SFTSREngine, _lcid, eLEXTYPE_PRIVATE8,
    SpeechPropertyResourceUsage, DISPID_SVIsUISupported, VARIANT_BOOL,
    DISPID_SWFEFormatTag, DISPID_SPAsCount, SPSNoun, SASPause,
    DISPID_SOTRemoveStorageFileName, SpeechCategoryRecognizers,
    ISpeechLexiconPronunciations, SGLexicalNoSpecialChars,
    SPSFunction, SPEI_RESERVED3, IUnknown, SpeechVoiceCategoryTTSRate,
    SPAO_RETAIN_AUDIO, SVSFIsXML, DISPID_SRRTLength,
    SAFTADPCM_44kHzStereo, SpStream, DISPID_SPPsItem, SP_VISEME_1,
    SVP_4, Speech_Default_Weight, DISPID_SOTCEnumerateTokens,
    DISPID_SRIsUISupported, DISPID_SMSALineId, SITooLoud, helpstring,
    eLEXTYPE_MORPHOLOGY, SVP_13, SPVOICESTATUS,
    DISPID_SRRGetXMLErrorInfo, SASStop, _FILETIME, SSFMOpenReadWrite,
    SpPhoneticAlphabetConverter, ISpPhoneticAlphabetConverter,
    DISPIDSPTSI_SelectionLength, SINone, DISPID_SWFEBlockAlign,
    DISPID_SRRTStreamTime, SAFTTrueSpeech_8kHz1BitMono, SDTProperty,
    SDTRule, ISpeechPhoneConverter, SAFTCCITT_uLaw_44kHzStereo,
    DISPID_SRGIsPronounceable, SRSActive, SAFT22kHz8BitMono,
    SpeechGrammarTagUnlimitedDictation, DISPID_SPPNumberOfElements,
    DISPID_SREmulateRecognition, SSFMOpenForRead,
    SpObjectTokenCategory, DISPID_SRCCreateGrammar, SREHypothesis,
    DISPID_SOTCDefault, eLEXTYPE_RESERVED8, SPAR_Medium,
    SPWF_SRENGINE, SpeechAudioProperties, DISPID_SGRId,
    DISPID_SDKGetStringValue, ISpPhoneConverter, SDKLDefaultLocation,
    SPSModifier, SRCS_Enabled, SPAR_Unknown, SpSharedRecognizer,
    DISPID_SAEventHandle, eLEXTYPE_PRIVATE12, DISPID_SVResume,
    DISPID_SGRSRule, ISpeechPhraseAlternates, DISPID_SRCEBookmark,
    SVP_8, DISPID_SCSBaseStream, DISPID_SPIEngineId, SPEI_RESERVED1,
    STCLocalServer, SVP_10, DISPID_SPEDisplayText, SLTApp,
    ISpPhoneticAlphabetSelection, ISpeechObjectToken,
    ISpeechXMLRecoResult, ISpObjectToken, SFTInput,
    DISPID_SDKDeleteValue, DISPID_SMSADeviceId, SGRSTTTextBuffer,
    STSF_FlagCreate, SPEI_WORD_BOUNDARY, SSFMCreate,
    DISPID_SLPPartOfSpeech, DISPID_SVSInputSentenceLength,
    SREStreamStart, SPBO_AHEAD, DISPID_SVGetAudioOutputs,
    DISPID_SRRRecoContext, SAFT16kHz8BitStereo, SVEWordBoundary,
    WAVEFORMATEX, DISPID_SPAs_NewEnum, SVSFNLPMask,
    SPINTERFERENCE_TOOQUIET, DISPID_SRCreateRecoContext, DISPID_SOTId,
    SAFT22kHz8BitStereo, SVSFVoiceMask, SPSLMA, SPEI_START_SR_STREAM,
    SpCustomStream, SSSPTRelativeToStart, SDKLLocalMachine,
    DISPID_SPIGetText, DISPID_SPPValue, SPINTERFERENCE_NONE,
    ISpeechAudioFormat, SVP_7, DISPID_SRCEEndStream, ISpMMSysAudio,
    SPWORDPRONUNCIATIONLIST, SpeechAudioFormatGUIDWave,
    DISPID_SMSAMMHandle, SLTUser, SREBookmark, DISPID_SLPPhoneIds,
    DISPID_SOTMatchesAttributes, SAFTCCITT_ALaw_22kHzMono,
    SDA_No_Trailing_Space, SPSHORTCUTPAIRLIST, DISPID_SRAudioInput,
    SVSFIsNotXML, _RemotableHandle, DISPID_SVSpeakCompleteEvent,
    SP_VISEME_5, SpeechVoiceSkipTypeSentence, DISPID_SPAPhraseInfo,
    DISPID_SABIEventBias, SPAUDIOSTATUS, DISPIDSPTSI_SelectionOffset,
    SpeechTokenKeyUI, SITooFast, SpObjectToken,
    SpeechPropertyHighConfidenceThreshold,
    SPWP_UNKNOWN_WORD_PRONOUNCEABLE, DISPID_SRCResume,
    SpeechTokenValueCLSID, DISPID_SLPs_NewEnum, DISPID_SPPParent,
    DISPID_SPELexicalForm, DISPID_SVEWord,
    DISPID_SRSNumberOfActiveRules, SVF_Emphasis,
    SPRS_ACTIVE_WITH_AUTO_PAUSE, ISpeechPhraseElements, SVP_5,
    typelib_path, SECFIgnoreCase, DISPID_SPRuleId,
    DISPID_SLGetPronunciations, DISPID_SPCPhoneToId, DISPID_SOTsItem,
    DISPID_SLPLangId, SLODynamic, SAFT44kHz8BitMono,
    eLEXTYPE_PRIVATE4, SP_VISEME_16, ISpeechFileStream,
    DISPID_SPIStartTime, SRERecoOtherContext,
    DISPID_SRCCreateResultFromMemory, eLEXTYPE_RESERVED7,
    DISPID_SLPType, SRATopLevel, SVEAllEvents, SP_VISEME_7,
    ISpeechDataKey, SRAORetainAudio, SVP_11,
    SPWP_KNOWN_WORD_PRONOUNCEABLE, SVP_14, SPEI_VOICE_CHANGE,
    ISpeechGrammarRuleState, DISPID_SPIElements, _LARGE_INTEGER,
    DISPID_SDKSetLongValue, SAFT8kHz8BitStereo, SP_VISEME_10,
    SDA_Consume_Leading_Spaces, SP_VISEME_14, SVF_Stressed,
    DISPID_SVAlertBoundary, ISpeechRecognizerStatus,
    SAFT44kHz16BitMono, SpLexicon, DISPID_SRCEventInterests,
    DISPID_SOTRemove, DISPID_SMSGetData, SpeechTokenKeyAttributes,
    DISPID_SOTCategory, DISPID_SPRsCount, DISPID_SASState,
    eLEXTYPE_USER_SHORTCUT, eLEXTYPE_PRIVATE13,
    DISPID_SPANumberOfElementsInResult, DISPID_SRCEAudioLevel,
    DISPID_SRCEInterference, SAFT24kHz8BitMono, SPEI_MAX_SR,
    SRTReSent, SPEI_FALSE_RECOGNITION, SP_VISEME_11,
    DISPID_SOTCreateInstance, DISPID_SLWPronunciations, SRAImport,
    DISPID_SGRSAddSpecialTransition, SpeechAudioVolume,
    DISPID_SRCEStartStream, DISPID_SGRName,
    SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN, DISPID_SVPriority,
    SPDKL_CurrentConfig, CoClass, SPFM_CREATE, SVEViseme,
    DISPID_SRAudioInputStream, DISPID_SPRFirstElement,
    DISPID_SRCESoundStart, ISpeechWaveFormatEx, SPSEMANTICERRORINFO,
    ISpeechPhraseProperties, SRERequestUI, SPAUDIOBUFFERINFO,
    DISPIDSPTSI_ActiveOffset, DISPID_SDKEnumKeys, ISpNotifySink,
    DISPID_SABIMinNotification, DISPID_SVEViseme, SPWT_PRONUNCIATION,
    eLEXTYPE_PRIVATE17, DISPID_SVSyncronousSpeakTimeout,
    ISpRecoGrammar2, ISpGrammarBuilder,
    SpeechRegistryLocalMachineRoot, DISPID_SRGetFormat,
    DISPID_SGRSTPropertyId, DISPID_SVVoice, eLEXTYPE_PRIVATE20,
    SpMMAudioIn, DISPID_SGRSAddWordTransition, SRTStandard,
    SPEI_PHONEME, ISpeechVoice, eLEXTYPE_PRIVATE16,
    SpeechPropertyLowConfidenceThreshold, SVEAudioLevel,
    SPEI_HYPOTHESIS, SAFT11kHz8BitStereo, STCRemoteServer,
    SPSMF_SRGS_SAPIPROPERTIES, ISpXMLRecoResult, SAFT44kHz8BitStereo,
    SAFTADPCM_22kHzStereo, SpNullPhoneConverter, ISpObjectWithToken,
    SVEStartInputStream, SpeechDictationTopicSpelling,
    ISpeechBaseStream, SPCT_SLEEP, DISPID_SVSInputSentencePosition,
    ISpeechAudioBufferInfo, ISpeechPhraseRule, DISPID_SPIProperties,
    SPWT_LEXICAL, DISPID_SGRSTNextState, DISPID_SDKCreateKey,
    SGSDisabled, DISPID_SLWLangId, eLEXTYPE_PRIVATE3,
    DISPID_SRCEAdaptation, SAFT48kHz8BitMono, DISPID_SRRSaveToMemory,
    SGDSActiveWithAutoPause, SpeechPropertyResponseSpeed,
    DISPID_SPACommit, SPINTERFERENCE_TOOLOUD, SpVoice,
    SpSharedRecoContext, DISPID_SLAddPronunciationByPhoneIds,
    SPEI_RESERVED2, SPEI_ACTIVE_CATEGORY_CHANGED,
    SAFTGSM610_11kHzMono, ISpeechGrammarRule, SAFTCCITT_uLaw_8kHzMono,
    DISPID_SPEsCount, DISPID_SGRSTText, SAFT16kHz16BitStereo,
    SPGS_DISABLED, SAFTCCITT_uLaw_22kHzMono, DISPID_SGRClear,
    DISPID_SPEsItem, DISPID_SBSWrite, DISPID_SPERequiredConfidence,
    DISPID_SPPsCount, SPAS_STOP, SPDKL_LocalMachine, SPPS_Function,
    DISPID_SVSpeakStream, SVSFParseMask, DISPID_SOTGetDescription,
    SVP_12, DISPID_SVEAudioLevel, SWPKnownWordPronounceable,
    DISPID_SRSSupportedLanguages, SAFT24kHz16BitMono, DISPID_SVStatus,
    SPPROPERTYINFO, SAFTCCITT_ALaw_8kHzMono, SpAudioFormat,
    DISPID_SPCLangId, ISpeechLexicon,
    SPSMF_SRGS_SEMANTICINTERPRETATION_W3C, SAFTCCITT_ALaw_11kHzStereo,
    SREPropertyNumChange, SBOPause, DISPID_SAFGuid,
    DISPID_SPEPronunciation, SVSFUnusedFlags, SPEI_RECOGNITION,
    SpeechRegistryUserRoot, SpeechPropertyNormalConfidenceThreshold,
    SPSERIALIZEDPHRASE, DISPID_SRCCmdMaxAlternates, eWORDTYPE_DELETED,
    SPRST_NUM_STATES, DISPID_SRCERecognitionForOtherContext, SPWORD,
    ISpeechPhraseProperty, SPEI_RESERVED6, SPEI_SR_RETAINEDAUDIO,
    SPEI_MAX_TTS, DISPID_SRSCurrentStreamPosition,
    ISpeechGrammarRuleStateTransition, DISPID_SOTsCount,
    SAFTCCITT_uLaw_44kHzMono, SRERecognition, HRESULT,
    DISPID_SPIGetDisplayAttributes, SPWORDLIST, SDKLCurrentConfig,
    SPSHT_OTHER, ISpeechRecognizer, SP_VISEME_4, SPSUnknown,
    DISPID_SRGCmdSetRuleIdState, IServiceProvider, eLEXTYPE_PRIVATE6,
    STSF_AppData, ISpeechGrammarRuleStateTransitions, SWTAdded,
    SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE, SRTAutopause,
    SAFTCCITT_uLaw_11kHzMono, SPAS_RUN, SRSEDone, SECFIgnoreKanaType,
    SPPHRASEPROPERTY, DISPID_SBSSeek, tagSPTEXTSELECTIONINFO,
    SPRST_INACTIVE_WITH_PURGE, SGRSTTWildcard, SPGS_ENABLED,
    DISPID_SLPsItem, SpeechAudioFormatGUIDText, DISPID_SVAudioOutput,
    DISPID_SDKEnumValues, DISPID_SOTDataKey, SRADefaultToActive,
    ISpRecoGrammar, SPPS_RESERVED4, SAFTNonStandardFormat,
    SAFTADPCM_11kHzStereo, SDKLCurrentUser, SAFT12kHz8BitMono,
    SPAR_High, ISpRecoContext, eLEXTYPE_PRIVATE10,
    SAFTGSM610_8kHzMono, ISpShortcut, SPEI_RESERVED5, SECFIgnoreWidth,
    SPTEXTSELECTIONINFO, DISPID_SABufferInfo, DISPID_SGRsAdd,
    SPCT_SUB_COMMAND, DISPID_SVSVisemeId, tagSPPROPERTYINFO,
    SPXRO_SML, DISPID_SRRecognizer, SWPUnknownWordPronounceable,
    SPEI_REQUEST_UI, SVP_9, STCAll, DISPID_SVWaitUntilDone,
    SGDSActiveUserDelimited, SPAO_NONE, SAFTCCITT_ALaw_22kHzStereo,
    DISPID_SVGetAudioInputs, DISPID_SRGDictationUnload,
    SpResourceManager, SpeechRecoProfileProperties,
    SPEI_END_SR_STREAM, ISpeechVoiceStatus, SpMMAudioOut, SRAExport,
    Library, __MIDL___MIDL_itf_sapi_0000_0020_0001,
    IInternetSecurityManager, SPEI_PROPERTY_NUM_CHANGE, SGLexical,
    SPRST_ACTIVE, SITooQuiet, DISPID_SASNonBlockingIO,
    ISpeechLexiconWords, DISPID_SRCVoice, SPRULE, SRARoot, SINoSignal,
    SPINTERFERENCE_NOSIGNAL, DISPID_SOTIsUISupported,
    SPEI_RECO_OTHER_CONTEXT, SVP_19, DISPID_SLWsCount,
    SAFT16kHz16BitMono, SPINTERFERENCE_NOISE, DISPID_SRCRetainedAudio,
    DISPID_SDKDeleteKey, DISPID_SRProfile, SBONone,
    SSFMCreateForWrite, SPINTERFERENCE_TOOSLOW, SpShortcut, COMMETHOD,
    SVPOver, SAFT32kHz8BitMono, eLEXTYPE_RESERVED6, SRTEmulated,
    SpeechPropertyComplexResponseSpeed, DISPID_SPIRetainedSizeBytes,
    SAFT16kHz8BitMono, SPBO_PAUSE, wireHWND,
    DISPID_SPPEngineConfidence, SPWORDPRONUNCIATION,
    SPPS_Interjection, SRSInactiveWithPurge,
    DISPID_SLRemovePronunciationByPhoneIds, SAFTCCITT_ALaw_11kHzMono,
    DISPID_SVSInputWordPosition, SVP_2, SpNotifyTranslator,
    DISPID_SRGCommit, ISpLexicon, SpMemoryStream,
    __MIDL_IWinTypes_0009, SPLO_STATIC, DISPID_SPPName,
    SAFTCCITT_uLaw_11kHzStereo, SPFM_OPEN_READONLY, SVF_None,
    DISPID_SPRuleChildren, SpMMAudioEnum, SASRun,
    SpeechPropertyAdaptationOn, SDTAlternates, DISPID_SOTDisplayUI,
    SVP_1, SPEI_PROPERTY_STRING_CHANGE, DISPID_SAStatus,
    DISPID_SGRsCommit, SREInterference, DISPID_SRRGetXMLResult,
    SAFTDefault, DISPID_SVVolume, DISPID_SRCSetAdaptationData,
    DISPID_SGRAddResource, ISpeechRecoResult2,
    DISPID_SVSLastBookmarkId, LONG_PTR, DISPID_SGRSTransitions,
    DISPID_SVSkip, ISpStreamFormat, DISPID_SPILanguageId,
    DISPID_SLWWord, DISPID_SPEActualConfidence, DISPID_SPIGrammarId,
    SVP_21, ISpSerializeState, ISpStream, SSSPTRelativeToEnd,
    DISPID_SRGCmdLoadFromResource, SREPhraseStart, SPSHT_Unknown,
    DISPID_SVDisplayUI, ISpeechRecoResult, SSTTDictation,
    SECLowConfidence, DISPID_SPRuleName, SpCompressedLexicon,
    SECNormalConfidence, ISpeechPhraseRules, DISPID_SVSpeak,
    SpeechTokenIdUserLexicon, SGRSTTEpsilon, DISPID_SPRuleConfidence,
    SAFTCCITT_uLaw_8kHzStereo, SPAR_Low, SVEVoiceChange,
    DISPID_SVSLastBookmark, SAFT44kHz16BitStereo,
    DISPID_SADefaultFormat, DISPID_SLPSymbolic,
    DISPID_SVSRunningState, DISPID_SABufferNotifySize, GUID,
    DISPID_SGRSTRule, SPBINARYGRAMMAR, DISPID_SRGDictationLoad,
    SRSEIsSpeaking, SSSPTRelativeToCurrentPosition, SPPS_NotOverriden,
    SITooSlow, SREStateChange, SECFEmulateResult, SVPAlert,
    DISPID_SGRsDynamic, DISPID_SRIsShared, DISPID_SGRInitialState,
    SpeechUserTraining, DISPID_SDKGetlongValue, SAFT11kHz8BitMono,
    SP_VISEME_13, SPEI_SR_BOOKMARK, SGPronounciation,
    DISPID_SPIAudioSizeTime, DISPID_SABIBufferSize,
    SpPhraseInfoBuilder, SREAudioLevel, DISPID_SLGetGenerationChange,
    SDTAudio, _ULARGE_INTEGER, DISPID_SRGSetWordSequenceData,
    ISpeechRecoGrammar, SRESoundStart, DISPID_SRDisplayUI,
    SAFT8kHz16BitMono, SPRST_INACTIVE, ISpeechLexiconPronunciation,
    SPPS_Noun, SREAdaptation, ISpeechAudio, SAFT11kHz16BitStereo,
    DISPID_SRGCmdLoadFromFile, DISPID_SPPId, SPVPRI_ALERT,
    _ISpeechVoiceEvents, SAFT22kHz16BitMono, eLEXTYPE_PRIVATE9,
    DISPID_SVEStreamStart, eLEXTYPE_RESERVED10, SAFT24kHz8BitStereo,
    DISPID_SRSAudioStatus, SECFNoSpecialChars, eLEXTYPE_PRIVATE1,
    SP_VISEME_8, SPPS_Noncontent, ISpeechResourceLoader,
    STSF_CommonAppData, tagSTATSTG, SPSNotOverriden,
    SPEI_START_INPUT_STREAM, DISPID_SPRuleParent,
    DISPID_SRRPhraseInfo, DISPID_SRSCurrentStreamNumber,
    DISPID_SVEventInterests, SGRSTTWord, SpeechCategoryVoices,
    SREAllEvents, _check_version, SSTTWildcard, ISpeechAudioStatus,
    DISPID_SLGetWords, DISPID_SMSSetData, SRADynamic, SP_VISEME_19,
    SVSFParseSapi, ISpeechRecoResultDispatch, SPEI_SR_PRIVATE,
    SECHighConfidence, SpeechCategoryPhoneConverters, SPBO_NONE,
    SAFT12kHz16BitMono, SINoise, SVP_20, SRAInterpreter,
    DISPIDSPTSI_ActiveLength, Speech_StreamPos_RealTime,
    DISPID_SRCERecognition, SP_VISEME_21, DISPID_SRGCmdSetRuleState,
    SRSInactive, DISPID_SOTCGetDataKey, IEnumString,
    DISPID_SPIAudioSizeBytes, SPSMF_SRGS_SEMANTICINTERPRETATION_MS,
    SPPHRASEELEMENT, SDA_Two_Trailing_Spaces, SAFTExtendedAudioFormat,
    DISPID_SPCIdToPhone, SAFT12kHz8BitStereo, DISPID_SAFType,
    DISPID_SPIEnginePrivateData, SRAONone, SVSFPersistXML,
    DISPID_SRRAudioFormat, DISPID_SWFEChannels,
    DISPID_SRGSetTextSelection, SPSHT_NotOverriden, eLEXTYPE_PRIVATE2,
    ISpeechObjectTokenCategory, SDTAll, DISPID_SVRate, WSTRING,
    dispid, SVPNormal, DISPID_SPRs_NewEnum, DISPID_SVEBookmark,
    DISPID_SRSetPropertyString, SAFT8kHz16BitStereo,
    SAFT11kHz16BitMono, ISpeechPhraseReplacement,
    SWPUnknownWordUnpronounceable, DISPID_SVSCurrentStreamNumber,
    DISPID_SRRTOffsetFromStart, ISpeechPhraseElement, SP_VISEME_15,
    SPEI_RECO_STATE_CHANGE, SpeechAddRemoveWord, SPDKL_CurrentUser,
    VARIANT, SREPrivate, DISPID_SPPs_NewEnum, SpeechEngineProperties,
    SPBO_TIME_UNITS, SAFTCCITT_ALaw_8kHzStereo, DISPID_SGRAttributes,
    BSTR, eLEXTYPE_PRIVATE19, eLEXTYPE_PRIVATE5, DISPID_SPEs_NewEnum,
    SAFTText, SPFM_OPEN_READWRITE, eLEXTYPE_VENDORLEXICON,
    DISPID_SPRules_NewEnum, SP_VISEME_12, DISPID_SBSRead,
    SPEI_TTS_BOOKMARK, DISPID_SRRDiscardResultInfo,
    DISPID_SRRSpeakAudio, SPRST_ACTIVE_ALWAYS,
    DISPID_SPERetainedSizeBytes, ISpDataKey, DISPID_SRGId,
    SP_VISEME_17, SAFT48kHz16BitMono, DISPID_SRGRules,
    SAFT12kHz16BitStereo, SDTReplacement, SDTLexicalForm,
    DISPID_SPEAudioStreamOffset, ISpStreamFormatConverter,
    SGDSInactive, SVP_18, DISPID_SRCPause,
    DISPID_SRCEPropertyStringChange, SVP_0, DISPID_SRCESoundEnd,
    SPVPRI_OVER, SP_VISEME_20, SPEI_SOUND_END, SAFT32kHz16BitStereo,
    SpInProcRecoContext, DISPID_SPPFirstElement, DISPID_SFSClose,
    SRESoundEnd, DISPID_SVESentenceBoundary, DISPID_SRCEEnginePrivate,
    DISPID_SLWs_NewEnum, SGRSTTRule, SpUnCompressedLexicon,
    DISPID_SGRSTType, DISPID_SRState, DISPID_SDKGetBinaryValue,
    DISPID_SRGDictationSetState, SAFTCCITT_ALaw_44kHzStereo,
    DISPID_SDKSetStringValue, DISPID_SRCEPhraseStart, ISpVoice,
    SPPS_Verb, SPSInterjection, DISPID_SVSLastResult,
    DISPID_SRCEHypothesis, DISPID_SLAddPronunciation, DISPID_SRStatus,
    ISpeechPhraseAlternate, SpeechCategoryRecoProfiles,
    ISpRecognizer2, ISpeechPhraseInfoBuilder, DISPID_SVSPhonemeId,
    SREStreamEnd, DISPID_SRRTimes, SPEI_TTS_PRIVATE, SDTPronunciation,
    DISPID_SPEAudioSizeBytes, SVSFDefault, SPEI_SR_AUDIO_LEVEL,
    DISPID_SRCRequestedUIType, SAFTNoAssignedFormat, SPCS_ENABLED,
    SP_VISEME_0, SPAS_PAUSE, DISPID_SRGState, SAFT8kHz8BitMono,
    SpeechTokenKeyFiles, DISPID_SRCERequestUI, DISPID_SWFEExtraData,
    DISPID_SOTSetId, SpPhoneConverter, ISpeechRecoContext,
    SPINTERFERENCE_TOOFAST, SAFT22kHz16BitStereo, SVSFIsFilename,
    ISpeechCustomStream, SPEI_UNDEFINED, SPPS_RESERVED3,
    eLEXTYPE_RESERVED9, SPEI_INTERFERENCE, SPWT_DISPLAY, SGSEnabled,
    DISPID_SPIAudioStreamPosition, DISPID_SASCurrentDevicePosition,
    STSF_LocalAppData, SPSERIALIZEDRESULT, eLEXTYPE_PRIVATE11,
    SPGS_EXCLUSIVE, ISpeechMemoryStream, Speech_StreamPos_Asap,
    SRSActiveAlways, SpInprocRecognizer, SpStreamFormatConverter,
    DISPID_SRCEFalseRecognition, Speech_Max_Word_Length,
    DISPID_SOTCSetId, DISPID_SRGetRecognizers,
    DISPID_SWFEAvgBytesPerSec, SGDSActive, SPEI_MIN_SR,
    DISPID_SAFSetWaveFormatEx, DISPID_SPISaveToMemory, SPRS_INACTIVE,
    SPXRO_Alternates_SML, SRTSMLTimeout, SPEI_MIN_TTS,
    SAFT32kHz8BitStereo, DISPID_SRCVoicePurgeEvent,
    DISPID_SRAllowVoiceFormatMatchingOnNextSet, DISPMETHOD,
    SAFTADPCM_22kHzMono, SVEEndInputStream, DISPID_SASFreeBufferSpace,
    SpeechCategoryAudioIn, SAFT48kHz16BitStereo, SVP_6
)


class SPADAPTATIONRELEVANCE(IntFlag):
    SPAR_Unknown = 0
    SPAR_Low = 1
    SPAR_Medium = 2
    SPAR_High = 3


class SPSHORTCUTTYPE(IntFlag):
    SPSHT_NotOverriden = -1
    SPSHT_Unknown = 0
    SPSHT_EMAIL = 4096
    SPSHT_OTHER = 8192
    SPPS_RESERVED1 = 12288
    SPPS_RESERVED2 = 16384
    SPPS_RESERVED3 = 20480
    SPPS_RESERVED4 = 61440


class SpeechRecognizerState(IntFlag):
    SRSInactive = 0
    SRSActive = 1
    SRSActiveAlways = 2
    SRSInactiveWithPurge = 3


class SpeechFormatType(IntFlag):
    SFTInput = 0
    SFTSREngine = 1


class SpeechAudioFormatType(IntFlag):
    SAFTDefault = -1
    SAFTNoAssignedFormat = 0
    SAFTText = 1
    SAFTNonStandardFormat = 2
    SAFTExtendedAudioFormat = 3
    SAFT8kHz8BitMono = 4
    SAFT8kHz8BitStereo = 5
    SAFT8kHz16BitMono = 6
    SAFT8kHz16BitStereo = 7
    SAFT11kHz8BitMono = 8
    SAFT11kHz8BitStereo = 9
    SAFT11kHz16BitMono = 10
    SAFT11kHz16BitStereo = 11
    SAFT12kHz8BitMono = 12
    SAFT12kHz8BitStereo = 13
    SAFT12kHz16BitMono = 14
    SAFT12kHz16BitStereo = 15
    SAFT16kHz8BitMono = 16
    SAFT16kHz8BitStereo = 17
    SAFT16kHz16BitMono = 18
    SAFT16kHz16BitStereo = 19
    SAFT22kHz8BitMono = 20
    SAFT22kHz8BitStereo = 21
    SAFT22kHz16BitMono = 22
    SAFT22kHz16BitStereo = 23
    SAFT24kHz8BitMono = 24
    SAFT24kHz8BitStereo = 25
    SAFT24kHz16BitMono = 26
    SAFT24kHz16BitStereo = 27
    SAFT32kHz8BitMono = 28
    SAFT32kHz8BitStereo = 29
    SAFT32kHz16BitMono = 30
    SAFT32kHz16BitStereo = 31
    SAFT44kHz8BitMono = 32
    SAFT44kHz8BitStereo = 33
    SAFT44kHz16BitMono = 34
    SAFT44kHz16BitStereo = 35
    SAFT48kHz8BitMono = 36
    SAFT48kHz8BitStereo = 37
    SAFT48kHz16BitMono = 38
    SAFT48kHz16BitStereo = 39
    SAFTTrueSpeech_8kHz1BitMono = 40
    SAFTCCITT_ALaw_8kHzMono = 41
    SAFTCCITT_ALaw_8kHzStereo = 42
    SAFTCCITT_ALaw_11kHzMono = 43
    SAFTCCITT_ALaw_11kHzStereo = 44
    SAFTCCITT_ALaw_22kHzMono = 45
    SAFTCCITT_ALaw_22kHzStereo = 46
    SAFTCCITT_ALaw_44kHzMono = 47
    SAFTCCITT_ALaw_44kHzStereo = 48
    SAFTCCITT_uLaw_8kHzMono = 49
    SAFTCCITT_uLaw_8kHzStereo = 50
    SAFTCCITT_uLaw_11kHzMono = 51
    SAFTCCITT_uLaw_11kHzStereo = 52
    SAFTCCITT_uLaw_22kHzMono = 53
    SAFTCCITT_uLaw_22kHzStereo = 54
    SAFTCCITT_uLaw_44kHzMono = 55
    SAFTCCITT_uLaw_44kHzStereo = 56
    SAFTADPCM_8kHzMono = 57
    SAFTADPCM_8kHzStereo = 58
    SAFTADPCM_11kHzMono = 59
    SAFTADPCM_11kHzStereo = 60
    SAFTADPCM_22kHzMono = 61
    SAFTADPCM_22kHzStereo = 62
    SAFTADPCM_44kHzMono = 63
    SAFTADPCM_44kHzStereo = 64
    SAFTGSM610_8kHzMono = 65
    SAFTGSM610_11kHzMono = 66
    SAFTGSM610_22kHzMono = 67
    SAFTGSM610_44kHzMono = 68


class DISPID_SpeechObjectToken(IntFlag):
    DISPID_SOTId = 1
    DISPID_SOTDataKey = 2
    DISPID_SOTCategory = 3
    DISPID_SOTGetDescription = 4
    DISPID_SOTSetId = 5
    DISPID_SOTGetAttribute = 6
    DISPID_SOTCreateInstance = 7
    DISPID_SOTRemove = 8
    DISPID_SOTGetStorageFileName = 9
    DISPID_SOTRemoveStorageFileName = 10
    DISPID_SOTIsUISupported = 11
    DISPID_SOTDisplayUI = 12
    DISPID_SOTMatchesAttributes = 13


class SpeechRuleAttributes(IntFlag):
    SRATopLevel = 1
    SRADefaultToActive = 2
    SRAExport = 4
    SRAImport = 8
    SRAInterpreter = 16
    SRADynamic = 32
    SRARoot = 64


class DISPID_SpeechDataKey(IntFlag):
    DISPID_SDKSetBinaryValue = 1
    DISPID_SDKGetBinaryValue = 2
    DISPID_SDKSetStringValue = 3
    DISPID_SDKGetStringValue = 4
    DISPID_SDKSetLongValue = 5
    DISPID_SDKGetlongValue = 6
    DISPID_SDKOpenKey = 7
    DISPID_SDKCreateKey = 8
    DISPID_SDKDeleteKey = 9
    DISPID_SDKDeleteValue = 10
    DISPID_SDKEnumKeys = 11
    DISPID_SDKEnumValues = 12


class SPLOADOPTIONS(IntFlag):
    SPLO_STATIC = 0
    SPLO_DYNAMIC = 1


class SPCATEGORYTYPE(IntFlag):
    SPCT_COMMAND = 0
    SPCT_DICTATION = 1
    SPCT_SLEEP = 2
    SPCT_SUB_COMMAND = 3
    SPCT_SUB_DICTATION = 4


class DISPID_SpeechObjectTokens(IntFlag):
    DISPID_SOTsCount = 1
    DISPID_SOTsItem = 0
    DISPID_SOTs_NewEnum = -4


class SPRULESTATE(IntFlag):
    SPRS_INACTIVE = 0
    SPRS_ACTIVE = 1
    SPRS_ACTIVE_WITH_AUTO_PAUSE = 3
    SPRS_ACTIVE_USER_DELIMITED = 4


class DISPID_SpeechObjectTokenCategory(IntFlag):
    DISPID_SOTCId = 1
    DISPID_SOTCDefault = 2
    DISPID_SOTCSetId = 3
    DISPID_SOTCGetDataKey = 4
    DISPID_SOTCEnumerateTokens = 5


class SpeechTokenContext(IntFlag):
    STCInprocServer = 1
    STCInprocHandler = 2
    STCLocalServer = 4
    STCRemoteServer = 16
    STCAll = 23


class DISPID_SpeechAudioFormat(IntFlag):
    DISPID_SAFType = 1
    DISPID_SAFGuid = 2
    DISPID_SAFGetWaveFormatEx = 3
    DISPID_SAFSetWaveFormatEx = 4


class SPPARTOFSPEECH(IntFlag):
    SPPS_NotOverriden = -1
    SPPS_Unknown = 0
    SPPS_Noun = 4096
    SPPS_Verb = 8192
    SPPS_Modifier = 12288
    SPPS_Function = 16384
    SPPS_Interjection = 20480
    SPPS_Noncontent = 24576
    SPPS_LMA = 28672
    SPPS_SuppressWord = 61440


class DISPID_SpeechBaseStream(IntFlag):
    DISPID_SBSFormat = 1
    DISPID_SBSRead = 2
    DISPID_SBSWrite = 3
    DISPID_SBSSeek = 4


class SPXMLRESULTOPTIONS(IntFlag):
    SPXRO_SML = 0
    SPXRO_Alternates_SML = 1


class DISPID_SpeechAudio(IntFlag):
    DISPID_SAStatus = 200
    DISPID_SABufferInfo = 201
    DISPID_SADefaultFormat = 202
    DISPID_SAVolume = 203
    DISPID_SABufferNotifySize = 204
    DISPID_SAEventHandle = 205
    DISPID_SASetState = 206


class SPWORDPRONOUNCEABLE(IntFlag):
    SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE = 0
    SPWP_UNKNOWN_WORD_PRONOUNCEABLE = 1
    SPWP_KNOWN_WORD_PRONOUNCEABLE = 2


class SPLEXICONTYPE(IntFlag):
    eLEXTYPE_USER = 1
    eLEXTYPE_APP = 2
    eLEXTYPE_VENDORLEXICON = 4
    eLEXTYPE_LETTERTOSOUND = 8
    eLEXTYPE_MORPHOLOGY = 16
    eLEXTYPE_RESERVED4 = 32
    eLEXTYPE_USER_SHORTCUT = 64
    eLEXTYPE_RESERVED6 = 128
    eLEXTYPE_RESERVED7 = 256
    eLEXTYPE_RESERVED8 = 512
    eLEXTYPE_RESERVED9 = 1024
    eLEXTYPE_RESERVED10 = 2048
    eLEXTYPE_PRIVATE1 = 4096
    eLEXTYPE_PRIVATE2 = 8192
    eLEXTYPE_PRIVATE3 = 16384
    eLEXTYPE_PRIVATE4 = 32768
    eLEXTYPE_PRIVATE5 = 65536
    eLEXTYPE_PRIVATE6 = 131072
    eLEXTYPE_PRIVATE7 = 262144
    eLEXTYPE_PRIVATE8 = 524288
    eLEXTYPE_PRIVATE9 = 1048576
    eLEXTYPE_PRIVATE10 = 2097152
    eLEXTYPE_PRIVATE11 = 4194304
    eLEXTYPE_PRIVATE12 = 8388608
    eLEXTYPE_PRIVATE13 = 16777216
    eLEXTYPE_PRIVATE14 = 33554432
    eLEXTYPE_PRIVATE15 = 67108864
    eLEXTYPE_PRIVATE16 = 134217728
    eLEXTYPE_PRIVATE17 = 268435456
    eLEXTYPE_PRIVATE18 = 536870912
    eLEXTYPE_PRIVATE19 = 1073741824
    eLEXTYPE_PRIVATE20 = -2147483648


class DISPID_SpeechMMSysAudio(IntFlag):
    DISPID_SMSADeviceId = 300
    DISPID_SMSALineId = 301
    DISPID_SMSAMMHandle = 302


class SPGRAMMARSTATE(IntFlag):
    SPGS_DISABLED = 0
    SPGS_ENABLED = 1
    SPGS_EXCLUSIVE = 3


class DISPID_SpeechFileStream(IntFlag):
    DISPID_SFSOpen = 100
    DISPID_SFSClose = 101


class DISPID_SpeechCustomStream(IntFlag):
    DISPID_SCSBaseStream = 100


class SPINTERFERENCE(IntFlag):
    SPINTERFERENCE_NONE = 0
    SPINTERFERENCE_NOISE = 1
    SPINTERFERENCE_NOSIGNAL = 2
    SPINTERFERENCE_TOOLOUD = 3
    SPINTERFERENCE_TOOQUIET = 4
    SPINTERFERENCE_TOOFAST = 5
    SPINTERFERENCE_TOOSLOW = 6
    SPINTERFERENCE_LATENCY_WARNING = 7
    SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN = 8
    SPINTERFERENCE_LATENCY_TRUNCATE_END = 9


class DISPID_SpeechMemoryStream(IntFlag):
    DISPID_SMSSetData = 100
    DISPID_SMSGetData = 101


class DISPID_SpeechAudioStatus(IntFlag):
    DISPID_SASFreeBufferSpace = 1
    DISPID_SASNonBlockingIO = 2
    DISPID_SASState = 3
    DISPID_SASCurrentSeekPosition = 4
    DISPID_SASCurrentDevicePosition = 5


class DISPID_SpeechAudioBufferInfo(IntFlag):
    DISPID_SABIMinNotification = 1
    DISPID_SABIBufferSize = 2
    DISPID_SABIEventBias = 3


class SpeechStreamSeekPositionType(IntFlag):
    SSSPTRelativeToStart = 0
    SSSPTRelativeToCurrentPosition = 1
    SSSPTRelativeToEnd = 2


class DISPID_SpeechWaveFormatEx(IntFlag):
    DISPID_SWFEFormatTag = 1
    DISPID_SWFEChannels = 2
    DISPID_SWFESamplesPerSec = 3
    DISPID_SWFEAvgBytesPerSec = 4
    DISPID_SWFEBlockAlign = 5
    DISPID_SWFEBitsPerSample = 6
    DISPID_SWFEExtraData = 7


class DISPID_SpeechVoice(IntFlag):
    DISPID_SVStatus = 1
    DISPID_SVVoice = 2
    DISPID_SVAudioOutput = 3
    DISPID_SVAudioOutputStream = 4
    DISPID_SVRate = 5
    DISPID_SVVolume = 6
    DISPID_SVAllowAudioOuputFormatChangesOnNextSet = 7
    DISPID_SVEventInterests = 8
    DISPID_SVPriority = 9
    DISPID_SVAlertBoundary = 10
    DISPID_SVSyncronousSpeakTimeout = 11
    DISPID_SVSpeak = 12
    DISPID_SVSpeakStream = 13
    DISPID_SVPause = 14
    DISPID_SVResume = 15
    DISPID_SVSkip = 16
    DISPID_SVGetVoices = 17
    DISPID_SVGetAudioOutputs = 18
    DISPID_SVWaitUntilDone = 19
    DISPID_SVSpeakCompleteEvent = 20
    DISPID_SVIsUISupported = 21
    DISPID_SVDisplayUI = 22


class SpeechGrammarWordType(IntFlag):
    SGDisplay = 0
    SGLexical = 1
    SGPronounciation = 2
    SGLexicalNoSpecialChars = 3


class SpeechSpecialTransitionType(IntFlag):
    SSTTWildcard = 1
    SSTTDictation = 2
    SSTTTextBuffer = 3


class SPAUDIOOPTIONS(IntFlag):
    SPAO_NONE = 0
    SPAO_RETAIN_AUDIO = 1


class DISPID_SpeechVoiceStatus(IntFlag):
    DISPID_SVSCurrentStreamNumber = 1
    DISPID_SVSLastStreamNumberQueued = 2
    DISPID_SVSLastResult = 3
    DISPID_SVSRunningState = 4
    DISPID_SVSInputWordPosition = 5
    DISPID_SVSInputWordLength = 6
    DISPID_SVSInputSentencePosition = 7
    DISPID_SVSInputSentenceLength = 8
    DISPID_SVSLastBookmark = 9
    DISPID_SVSLastBookmarkId = 10
    DISPID_SVSPhonemeId = 11
    DISPID_SVSVisemeId = 12


class SpeechVisemeFeature(IntFlag):
    SVF_None = 0
    SVF_Stressed = 1
    SVF_Emphasis = 2


class SpeechVisemeType(IntFlag):
    SVP_0 = 0
    SVP_1 = 1
    SVP_2 = 2
    SVP_3 = 3
    SVP_4 = 4
    SVP_5 = 5
    SVP_6 = 6
    SVP_7 = 7
    SVP_8 = 8
    SVP_9 = 9
    SVP_10 = 10
    SVP_11 = 11
    SVP_12 = 12
    SVP_13 = 13
    SVP_14 = 14
    SVP_15 = 15
    SVP_16 = 16
    SVP_17 = 17
    SVP_18 = 18
    SVP_19 = 19
    SVP_20 = 20
    SVP_21 = 21


class SpeechDataKeyLocation(IntFlag):
    SDKLDefaultLocation = 0
    SDKLCurrentUser = 1
    SDKLLocalMachine = 2
    SDKLCurrentConfig = 5


class SpeechGrammarRuleStateTransitionType(IntFlag):
    SGRSTTEpsilon = 0
    SGRSTTWord = 1
    SGRSTTRule = 2
    SGRSTTDictation = 3
    SGRSTTWildcard = 4
    SGRSTTTextBuffer = 5


class DISPID_SpeechVoiceEvent(IntFlag):
    DISPID_SVEStreamStart = 1
    DISPID_SVEStreamEnd = 2
    DISPID_SVEVoiceChange = 3
    DISPID_SVEBookmark = 4
    DISPID_SVEWord = 5
    DISPID_SVEPhoneme = 6
    DISPID_SVESentenceBoundary = 7
    DISPID_SVEViseme = 8
    DISPID_SVEAudioLevel = 9
    DISPID_SVEEnginePrivate = 10


class SPWORDTYPE(IntFlag):
    eWORDTYPE_ADDED = 1
    eWORDTYPE_DELETED = 2


class DISPID_SpeechRecognizer(IntFlag):
    DISPID_SRRecognizer = 1
    DISPID_SRAllowAudioInputFormatChangesOnNextSet = 2
    DISPID_SRAudioInput = 3
    DISPID_SRAudioInputStream = 4
    DISPID_SRIsShared = 5
    DISPID_SRState = 6
    DISPID_SRStatus = 7
    DISPID_SRProfile = 8
    DISPID_SREmulateRecognition = 9
    DISPID_SRCreateRecoContext = 10
    DISPID_SRGetFormat = 11
    DISPID_SRSetPropertyNumber = 12
    DISPID_SRGetPropertyNumber = 13
    DISPID_SRSetPropertyString = 14
    DISPID_SRGetPropertyString = 15
    DISPID_SRIsUISupported = 16
    DISPID_SRDisplayUI = 17
    DISPID_SRGetRecognizers = 18
    DISPID_SVGetAudioInputs = 19
    DISPID_SVGetProfiles = 20


class SpeechTokenShellFolder(IntFlag):
    STSF_AppData = 26
    STSF_LocalAppData = 28
    STSF_CommonAppData = 35
    STSF_FlagCreate = 32768


class SpeechEmulationCompareFlags(IntFlag):
    SECFIgnoreCase = 1
    SECFIgnoreKanaType = 65536
    SECFIgnoreWidth = 131072
    SECFNoSpecialChars = 536870912
    SECFEmulateResult = 1073741824
    SECFDefault = 196609


class SPBOOKMARKOPTIONS(IntFlag):
    SPBO_NONE = 0
    SPBO_PAUSE = 1
    SPBO_AHEAD = 2
    SPBO_TIME_UNITS = 4


class SpeechAudioState(IntFlag):
    SASClosed = 0
    SASStop = 1
    SASPause = 2
    SASRun = 3


class SPCONTEXTSTATE(IntFlag):
    SPCS_DISABLED = 0
    SPCS_ENABLED = 1


class DISPID_SpeechRecognizerStatus(IntFlag):
    DISPID_SRSAudioStatus = 1
    DISPID_SRSCurrentStreamPosition = 2
    DISPID_SRSCurrentStreamNumber = 3
    DISPID_SRSNumberOfActiveRules = 4
    DISPID_SRSClsidEngine = 5
    DISPID_SRSSupportedLanguages = 6


class SPWAVEFORMATTYPE(IntFlag):
    SPWF_INPUT = 0
    SPWF_SRENGINE = 1


class SpeechVoiceEvents(IntFlag):
    SVEStartInputStream = 2
    SVEEndInputStream = 4
    SVEVoiceChange = 8
    SVEBookmark = 16
    SVEWordBoundary = 32
    SVEPhoneme = 64
    SVESentenceBoundary = 128
    SVEViseme = 256
    SVEAudioLevel = 512
    SVEPrivate = 32768
    SVEAllEvents = 33790


class SpeechStreamFileMode(IntFlag):
    SSFMOpenForRead = 0
    SSFMOpenReadWrite = 1
    SSFMCreate = 2
    SSFMCreateForWrite = 3


class SpeechBookmarkOptions(IntFlag):
    SBONone = 0
    SBOPause = 1


class DISPID_SpeechRecoResultTimes(IntFlag):
    DISPID_SRRTStreamTime = 1
    DISPID_SRRTLength = 2
    DISPID_SRRTTickCount = 3
    DISPID_SRRTOffsetFromStart = 4


class DISPID_SpeechRecoContext(IntFlag):
    DISPID_SRCRecognizer = 1
    DISPID_SRCAudioInInterferenceStatus = 2
    DISPID_SRCRequestedUIType = 3
    DISPID_SRCVoice = 4
    DISPID_SRAllowVoiceFormatMatchingOnNextSet = 5
    DISPID_SRCVoicePurgeEvent = 6
    DISPID_SRCEventInterests = 7
    DISPID_SRCCmdMaxAlternates = 8
    DISPID_SRCState = 9
    DISPID_SRCRetainedAudio = 10
    DISPID_SRCRetainedAudioFormat = 11
    DISPID_SRCPause = 12
    DISPID_SRCResume = 13
    DISPID_SRCCreateGrammar = 14
    DISPID_SRCCreateResultFromMemory = 15
    DISPID_SRCBookmark = 16
    DISPID_SRCSetAdaptationData = 17


class SPVISEMES(IntFlag):
    SP_VISEME_0 = 0
    SP_VISEME_1 = 1
    SP_VISEME_2 = 2
    SP_VISEME_3 = 3
    SP_VISEME_4 = 4
    SP_VISEME_5 = 5
    SP_VISEME_6 = 6
    SP_VISEME_7 = 7
    SP_VISEME_8 = 8
    SP_VISEME_9 = 9
    SP_VISEME_10 = 10
    SP_VISEME_11 = 11
    SP_VISEME_12 = 12
    SP_VISEME_13 = 13
    SP_VISEME_14 = 14
    SP_VISEME_15 = 15
    SP_VISEME_16 = 16
    SP_VISEME_17 = 17
    SP_VISEME_18 = 18
    SP_VISEME_19 = 19
    SP_VISEME_20 = 20
    SP_VISEME_21 = 21


class SpeechRecognitionType(IntFlag):
    SRTStandard = 0
    SRTAutopause = 1
    SRTEmulated = 2
    SRTSMLTimeout = 4
    SRTExtendableParse = 8
    SRTReSent = 16


class SpeechInterference(IntFlag):
    SINone = 0
    SINoise = 1
    SINoSignal = 2
    SITooLoud = 3
    SITooQuiet = 4
    SITooFast = 5
    SITooSlow = 6


class DISPID_SpeechPhraseAlternate(IntFlag):
    DISPID_SPARecoResult = 1
    DISPID_SPAStartElementInResult = 2
    DISPID_SPANumberOfElementsInResult = 3
    DISPID_SPAPhraseInfo = 4
    DISPID_SPACommit = 5


class SpeechEngineConfidence(IntFlag):
    SECLowConfidence = -1
    SECNormalConfidence = 0
    SECHighConfidence = 1


class SPGRAMMARWORDTYPE(IntFlag):
    SPWT_DISPLAY = 0
    SPWT_LEXICAL = 1
    SPWT_PRONUNCIATION = 2
    SPWT_LEXICAL_NO_SPECIAL_CHARS = 3


class SpeechVoicePriority(IntFlag):
    SVPNormal = 0
    SVPAlert = 1
    SVPOver = 2


class DISPID_SpeechPhraseAlternates(IntFlag):
    DISPID_SPAsCount = 1
    DISPID_SPAsItem = 0
    DISPID_SPAs_NewEnum = -4


class SPSEMANTICFORMAT(IntFlag):
    SPSMF_SAPI_PROPERTIES = 0
    SPSMF_SRGS_SEMANTICINTERPRETATION_MS = 1
    SPSMF_SRGS_SAPIPROPERTIES = 2
    SPSMF_UPS = 4
    SPSMF_SRGS_SEMANTICINTERPRETATION_W3C = 8


class SpeechLoadOption(IntFlag):
    SLOStatic = 0
    SLODynamic = 1


class DISPID_SpeechPhraseInfo(IntFlag):
    DISPID_SPILanguageId = 1
    DISPID_SPIGrammarId = 2
    DISPID_SPIStartTime = 3
    DISPID_SPIAudioStreamPosition = 4
    DISPID_SPIAudioSizeBytes = 5
    DISPID_SPIRetainedSizeBytes = 6
    DISPID_SPIAudioSizeTime = 7
    DISPID_SPIRule = 8
    DISPID_SPIProperties = 9
    DISPID_SPIElements = 10
    DISPID_SPIReplacements = 11
    DISPID_SPIEngineId = 12
    DISPID_SPIEnginePrivateData = 13
    DISPID_SPISaveToMemory = 14
    DISPID_SPIGetText = 15
    DISPID_SPIGetDisplayAttributes = 16


class DISPIDSPRG(IntFlag):
    DISPID_SRGId = 1
    DISPID_SRGRecoContext = 2
    DISPID_SRGState = 3
    DISPID_SRGRules = 4
    DISPID_SRGReset = 5
    DISPID_SRGCommit = 6
    DISPID_SRGCmdLoadFromFile = 7
    DISPID_SRGCmdLoadFromObject = 8
    DISPID_SRGCmdLoadFromResource = 9
    DISPID_SRGCmdLoadFromMemory = 10
    DISPID_SRGCmdLoadFromProprietaryGrammar = 11
    DISPID_SRGCmdSetRuleState = 12
    DISPID_SRGCmdSetRuleIdState = 13
    DISPID_SRGDictationLoad = 14
    DISPID_SRGDictationUnload = 15
    DISPID_SRGDictationSetState = 16
    DISPID_SRGSetWordSequenceData = 17
    DISPID_SRGSetTextSelection = 18
    DISPID_SRGIsPronounceable = 19


class SPDATAKEYLOCATION(IntFlag):
    SPDKL_DefaultLocation = 0
    SPDKL_CurrentUser = 1
    SPDKL_LocalMachine = 2
    SPDKL_CurrentConfig = 5


class SpeechRuleState(IntFlag):
    SGDSInactive = 0
    SGDSActive = 1
    SGDSActiveWithAutoPause = 3
    SGDSActiveUserDelimited = 4


class SpeechVoiceSpeakFlags(IntFlag):
    SVSFDefault = 0
    SVSFlagsAsync = 1
    SVSFPurgeBeforeSpeak = 2
    SVSFIsFilename = 4
    SVSFIsXML = 8
    SVSFIsNotXML = 16
    SVSFPersistXML = 32
    SVSFNLPSpeakPunc = 64
    SVSFParseSapi = 128
    SVSFParseSsml = 256
    SVSFParseAutodetect = 0
    SVSFNLPMask = 64
    SVSFParseMask = 384
    SVSFVoiceMask = 511
    SVSFUnusedFlags = -512


class SpeechDiscardType(IntFlag):
    SDTProperty = 1
    SDTReplacement = 2
    SDTRule = 4
    SDTDisplayText = 8
    SDTLexicalForm = 16
    SDTPronunciation = 32
    SDTAudio = 64
    SDTAlternates = 128
    SDTAll = 255


class DISPID_SpeechPhraseElement(IntFlag):
    DISPID_SPEAudioTimeOffset = 1
    DISPID_SPEAudioSizeTime = 2
    DISPID_SPEAudioStreamOffset = 3
    DISPID_SPEAudioSizeBytes = 4
    DISPID_SPERetainedStreamOffset = 5
    DISPID_SPERetainedSizeBytes = 6
    DISPID_SPEDisplayText = 7
    DISPID_SPELexicalForm = 8
    DISPID_SPEPronunciation = 9
    DISPID_SPEDisplayAttributes = 10
    DISPID_SPERequiredConfidence = 11
    DISPID_SPEActualConfidence = 12
    DISPID_SPEEngineConfidence = 13


class DISPID_SpeechRecoContextEvents(IntFlag):
    DISPID_SRCEStartStream = 1
    DISPID_SRCEEndStream = 2
    DISPID_SRCEBookmark = 3
    DISPID_SRCESoundStart = 4
    DISPID_SRCESoundEnd = 5
    DISPID_SRCEPhraseStart = 6
    DISPID_SRCERecognition = 7
    DISPID_SRCEHypothesis = 8
    DISPID_SRCEPropertyNumberChange = 9
    DISPID_SRCEPropertyStringChange = 10
    DISPID_SRCEFalseRecognition = 11
    DISPID_SRCEInterference = 12
    DISPID_SRCERequestUI = 13
    DISPID_SRCERecognizerStateChange = 14
    DISPID_SRCEAdaptation = 15
    DISPID_SRCERecognitionForOtherContext = 16
    DISPID_SRCEAudioLevel = 17
    DISPID_SRCEEnginePrivate = 18


class SPVPRIORITY(IntFlag):
    SPVPRI_NORMAL = 0
    SPVPRI_ALERT = 1
    SPVPRI_OVER = 2


class SpeechLexiconType(IntFlag):
    SLTUser = 1
    SLTApp = 2


class SpeechPartOfSpeech(IntFlag):
    SPSNotOverriden = -1
    SPSUnknown = 0
    SPSNoun = 4096
    SPSVerb = 8192
    SPSModifier = 12288
    SPSFunction = 16384
    SPSInterjection = 20480
    SPSLMA = 28672
    SPSSuppressWord = 61440


class DISPID_SpeechPhraseElements(IntFlag):
    DISPID_SPEsCount = 1
    DISPID_SPEsItem = 0
    DISPID_SPEs_NewEnum = -4


class SPEVENTENUM(IntFlag):
    SPEI_UNDEFINED = 0
    SPEI_START_INPUT_STREAM = 1
    SPEI_END_INPUT_STREAM = 2
    SPEI_VOICE_CHANGE = 3
    SPEI_TTS_BOOKMARK = 4
    SPEI_WORD_BOUNDARY = 5
    SPEI_PHONEME = 6
    SPEI_SENTENCE_BOUNDARY = 7
    SPEI_VISEME = 8
    SPEI_TTS_AUDIO_LEVEL = 9
    SPEI_TTS_PRIVATE = 15
    SPEI_MIN_TTS = 1
    SPEI_MAX_TTS = 15
    SPEI_END_SR_STREAM = 34
    SPEI_SOUND_START = 35
    SPEI_SOUND_END = 36
    SPEI_PHRASE_START = 37
    SPEI_RECOGNITION = 38
    SPEI_HYPOTHESIS = 39
    SPEI_SR_BOOKMARK = 40
    SPEI_PROPERTY_NUM_CHANGE = 41
    SPEI_PROPERTY_STRING_CHANGE = 42
    SPEI_FALSE_RECOGNITION = 43
    SPEI_INTERFERENCE = 44
    SPEI_REQUEST_UI = 45
    SPEI_RECO_STATE_CHANGE = 46
    SPEI_ADAPTATION = 47
    SPEI_START_SR_STREAM = 48
    SPEI_RECO_OTHER_CONTEXT = 49
    SPEI_SR_AUDIO_LEVEL = 50
    SPEI_SR_RETAINEDAUDIO = 51
    SPEI_SR_PRIVATE = 52
    SPEI_ACTIVE_CATEGORY_CHANGED = 53
    SPEI_RESERVED5 = 54
    SPEI_RESERVED6 = 55
    SPEI_MIN_SR = 34
    SPEI_MAX_SR = 55
    SPEI_RESERVED1 = 30
    SPEI_RESERVED2 = 33
    SPEI_RESERVED3 = 63


class SpeechWordPronounceable(IntFlag):
    SWPUnknownWordUnpronounceable = 0
    SWPUnknownWordPronounceable = 1
    SWPKnownWordPronounceable = 2


class DISPID_SpeechPhraseReplacement(IntFlag):
    DISPID_SPRDisplayAttributes = 1
    DISPID_SPRText = 2
    DISPID_SPRFirstElement = 3
    DISPID_SPRNumberOfElements = 4


class SpeechRecoEvents(IntFlag):
    SREStreamEnd = 1
    SRESoundStart = 2
    SRESoundEnd = 4
    SREPhraseStart = 8
    SRERecognition = 16
    SREHypothesis = 32
    SREBookmark = 64
    SREPropertyNumChange = 128
    SREPropertyStringChange = 256
    SREFalseRecognition = 512
    SREInterference = 1024
    SRERequestUI = 2048
    SREStateChange = 4096
    SREAdaptation = 8192
    SREStreamStart = 16384
    SRERecoOtherContext = 32768
    SREAudioLevel = 65536
    SREPrivate = 262144
    SREAllEvents = 393215


class SpeechRecoContextState(IntFlag):
    SRCS_Disabled = 0
    SRCS_Enabled = 1


class SpeechRetainedAudioOptions(IntFlag):
    SRAONone = 0
    SRAORetainAudio = 1


class DISPID_SpeechGrammarRule(IntFlag):
    DISPID_SGRAttributes = 1
    DISPID_SGRInitialState = 2
    DISPID_SGRName = 3
    DISPID_SGRId = 4
    DISPID_SGRClear = 5
    DISPID_SGRAddResource = 6
    DISPID_SGRAddState = 7


class DISPID_SpeechPhraseReplacements(IntFlag):
    DISPID_SPRsCount = 1
    DISPID_SPRsItem = 0
    DISPID_SPRs_NewEnum = -4


class SpeechDisplayAttributes(IntFlag):
    SDA_No_Trailing_Space = 0
    SDA_One_Trailing_Space = 2
    SDA_Two_Trailing_Spaces = 4
    SDA_Consume_Leading_Spaces = 8


class DISPID_SpeechPhraseProperty(IntFlag):
    DISPID_SPPName = 1
    DISPID_SPPId = 2
    DISPID_SPPValue = 3
    DISPID_SPPFirstElement = 4
    DISPID_SPPNumberOfElements = 5
    DISPID_SPPEngineConfidence = 6
    DISPID_SPPConfidence = 7
    DISPID_SPPParent = 8
    DISPID_SPPChildren = 9


class DISPID_SpeechGrammarRules(IntFlag):
    DISPID_SGRsCount = 1
    DISPID_SGRsDynamic = 2
    DISPID_SGRsAdd = 3
    DISPID_SGRsCommit = 4
    DISPID_SGRsCommitAndSave = 5
    DISPID_SGRsFindRule = 6
    DISPID_SGRsItem = 0
    DISPID_SGRs_NewEnum = -4


class _SPAUDIOSTATE(IntFlag):
    SPAS_CLOSED = 0
    SPAS_STOP = 1
    SPAS_PAUSE = 2
    SPAS_RUN = 3


class DISPID_SpeechPhraseProperties(IntFlag):
    DISPID_SPPsCount = 1
    DISPID_SPPsItem = 0
    DISPID_SPPs_NewEnum = -4


class DISPID_SpeechGrammarRuleState(IntFlag):
    DISPID_SGRSRule = 1
    DISPID_SGRSTransitions = 2
    DISPID_SGRSAddWordTransition = 3
    DISPID_SGRSAddRuleTransition = 4
    DISPID_SGRSAddSpecialTransition = 5


class DISPID_SpeechPhraseRule(IntFlag):
    DISPID_SPRuleName = 1
    DISPID_SPRuleId = 2
    DISPID_SPRuleFirstElement = 3
    DISPID_SPRuleNumberOfElements = 4
    DISPID_SPRuleParent = 5
    DISPID_SPRuleChildren = 6
    DISPID_SPRuleConfidence = 7
    DISPID_SPRuleEngineConfidence = 8


class SpeechWordType(IntFlag):
    SWTAdded = 1
    SWTDeleted = 2


class DISPID_SpeechGrammarRuleStateTransitions(IntFlag):
    DISPID_SGRSTsCount = 1
    DISPID_SGRSTsItem = 0
    DISPID_SGRSTs_NewEnum = -4


class DISPID_SpeechGrammarRuleStateTransition(IntFlag):
    DISPID_SGRSTType = 1
    DISPID_SGRSTText = 2
    DISPID_SGRSTRule = 3
    DISPID_SGRSTWeight = 4
    DISPID_SGRSTPropertyName = 5
    DISPID_SGRSTPropertyId = 6
    DISPID_SGRSTPropertyValue = 7
    DISPID_SGRSTNextState = 8


class DISPID_SpeechPhraseRules(IntFlag):
    DISPID_SPRulesCount = 1
    DISPID_SPRulesItem = 0
    DISPID_SPRules_NewEnum = -4


class DISPID_SpeechLexicon(IntFlag):
    DISPID_SLGenerationId = 1
    DISPID_SLGetWords = 2
    DISPID_SLAddPronunciation = 3
    DISPID_SLAddPronunciationByPhoneIds = 4
    DISPID_SLRemovePronunciation = 5
    DISPID_SLRemovePronunciationByPhoneIds = 6
    DISPID_SLGetPronunciations = 7
    DISPID_SLGetGenerationChange = 8


class DISPIDSPTSI(IntFlag):
    DISPIDSPTSI_ActiveOffset = 1
    DISPIDSPTSI_ActiveLength = 2
    DISPIDSPTSI_SelectionOffset = 3
    DISPIDSPTSI_SelectionLength = 4


class DISPID_SpeechLexiconWords(IntFlag):
    DISPID_SLWsCount = 1
    DISPID_SLWsItem = 0
    DISPID_SLWs_NewEnum = -4


class DISPID_SpeechRecoResult(IntFlag):
    DISPID_SRRRecoContext = 1
    DISPID_SRRTimes = 2
    DISPID_SRRAudioFormat = 3
    DISPID_SRRPhraseInfo = 4
    DISPID_SRRAlternates = 5
    DISPID_SRRAudio = 6
    DISPID_SRRSpeakAudio = 7
    DISPID_SRRSaveToMemory = 8
    DISPID_SRRDiscardResultInfo = 9


class DISPID_SpeechLexiconWord(IntFlag):
    DISPID_SLWLangId = 1
    DISPID_SLWType = 2
    DISPID_SLWWord = 3
    DISPID_SLWPronunciations = 4


class DISPID_SpeechLexiconProns(IntFlag):
    DISPID_SLPsCount = 1
    DISPID_SLPsItem = 0
    DISPID_SLPs_NewEnum = -4


class DISPID_SpeechXMLRecoResult(IntFlag):
    DISPID_SRRGetXMLResult = 10
    DISPID_SRRGetXMLErrorInfo = 11


class SpeechRunState(IntFlag):
    SRSEDone = 1
    SRSEIsSpeaking = 2


class DISPID_SpeechLexiconPronunciation(IntFlag):
    DISPID_SLPType = 1
    DISPID_SLPLangId = 2
    DISPID_SLPPartOfSpeech = 3
    DISPID_SLPPhoneIds = 4
    DISPID_SLPSymbolic = 5


class SPRECOSTATE(IntFlag):
    SPRST_INACTIVE = 0
    SPRST_ACTIVE = 1
    SPRST_ACTIVE_ALWAYS = 2
    SPRST_INACTIVE_WITH_PURGE = 3
    SPRST_NUM_STATES = 4


class DISPID_SpeechPhoneConverter(IntFlag):
    DISPID_SPCLangId = 1
    DISPID_SPCPhoneToId = 2
    DISPID_SPCIdToPhone = 3


class DISPID_SpeechRecoResult2(IntFlag):
    DISPID_SRRSetTextFeedback = 12


class SPFILEMODE(IntFlag):
    SPFM_OPEN_READONLY = 0
    SPFM_OPEN_READWRITE = 1
    SPFM_CREATE = 2
    SPFM_CREATE_ALWAYS = 3
    SPFM_NUM_MODES = 4


class SpeechGrammarState(IntFlag):
    SGSEnabled = 1
    SGSDisabled = 0
    SGSExclusive = 3


class DISPID_SpeechPhraseBuilder(IntFlag):
    DISPID_SPPBRestorePhraseFromMemory = 1


SPSTREAMFORMATTYPE = SPWAVEFORMATTYPE
SPAUDIOSTATE = _SPAUDIOSTATE


__all__ = [
    'SPVISEMES', 'DISPID_SpeechVoice', 'DISPID_SRGetPropertyString',
    'STCInprocHandler', 'ISpeechAudioBufferInfo', 'ISpeechPhraseRule',
    'DISPID_SPIProperties', 'SPWF_INPUT', 'SpeechCategoryAudioOut',
    'SPWT_LEXICAL', 'ISpResourceManager', 'SPSMF_SAPI_PROPERTIES',
    'SpeechBookmarkOptions', 'DISPID_SGRSTNextState',
    'DISPID_SDKCreateKey', 'SGSDisabled', 'SPLO_DYNAMIC',
    'DISPID_SDKSetBinaryValue', 'DISPID_SLWLangId',
    'SAFT48kHz8BitStereo', 'SVEPhoneme', 'SPEVENT', 'SPPHRASE',
    'UINT_PTR', 'eLEXTYPE_PRIVATE3', 'SPCATEGORYTYPE',
    'DISPID_SRCEAdaptation', 'DISPID_SpeechLexiconWord',
    'SPINTERFERENCE_LATENCY_TRUNCATE_END', 'SpeechTokenShellFolder',
    'SPADAPTATIONRELEVANCE', 'SVP_3', 'DISPID_SVEPhoneme',
    'SAFT48kHz8BitMono', 'ISpProperties', 'SVP_17',
    'DISPID_SRGCmdLoadFromObject', 'SpWaveFormatEx',
    'SGDSActiveWithAutoPause', 'DISPID_SRRSaveToMemory',
    'SGSExclusive', 'DISPID_SOTs_NewEnum',
    'SpeechPropertyResponseSpeed', 'DISPID_SOTGetAttribute',
    'DISPID_SGRsCount', 'DISPID_SGRSTPropertyName', 'ISpRecoContext2',
    'DISPID_SpeechRecoResult2', 'SPRECOGNIZERSTATUS',
    'DISPID_SPACommit', 'SPFM_NUM_MODES', 'SPCT_COMMAND',
    'SP_VISEME_3', 'SPINTERFERENCE_TOOLOUD', 'SLOStatic', 'SpVoice',
    'SpSharedRecoContext', 'ISpAudio', 'DISPID_SGRSAddRuleTransition',
    'DISPID_SLAddPronunciationByPhoneIds', 'SPEI_RESERVED2', 'SVP_15',
    'SPEI_ACTIVE_CATEGORY_CHANGED', 'SAFTGSM610_11kHzMono',
    'ISpeechGrammarRule', 'SP_VISEME_18', 'SAFTCCITT_uLaw_8kHzMono',
    'DISPID_SPEsCount', 'DISPID_SOTCId', 'SpeechAllElements',
    'DISPID_SpeechPhraseElement', 'DISPID_SGRSTText',
    'DISPID_SVAudioOutputStream', 'DISPID_SVSLastStreamNumberQueued',
    'ISpeechGrammarRules', 'SPCT_SUB_DICTATION',
    'SAFT16kHz16BitStereo', 'eLEXTYPE_USER', 'SPPS_LMA',
    'SPGS_DISABLED', 'SAFTCCITT_uLaw_22kHzMono',
    'DISPID_SRCRetainedAudioFormat', 'SPGRAMMARSTATE',
    'DISPID_SVSInputWordLength', 'DISPID_SpeechLexicon',
    'ISpEventSource', 'SAFTCCITT_ALaw_44kHzMono',
    'DISPID_SVGetVoices', 'SVSFPurgeBeforeSpeak', 'SPSHT_EMAIL',
    'DISPID_SPEsItem', 'DISPID_SRCEPropertyNumberChange',
    'DISPID_SGRClear', 'DISPID_SLWsItem', 'SpeechVoicePriority',
    'SpeechRetainedAudioOptions', 'DISPID_SBSWrite',
    'SpeechGrammarWordType', 'DISPID_SPERequiredConfidence',
    'eWORDTYPE_ADDED', 'SpeechGrammarTagWildcard', 'DISPID_SPPsCount',
    'SPAS_STOP', 'SPSSuppressWord', 'DISPID_SVEStreamEnd',
    'SPDKL_LocalMachine', 'DISPID_SpeechAudioStatus',
    'DISPID_SPRsItem', 'SPPS_Function', 'DISPID_SVSpeakStream',
    'SVSFParseMask', 'DISPID_SGRSTWeight', 'DISPID_SOTGetDescription',
    'DISPID_SVPause', 'IInternetSecurityMgrSite', 'SVP_12',
    'SPPS_Unknown', 'DISPID_SVEAudioLevel',
    'DISPID_SRGCmdLoadFromProprietaryGrammar',
    'DISPID_SRSSupportedLanguages', 'SWPKnownWordPronounceable',
    'ISpeechObjectTokens', 'eLEXTYPE_PRIVATE18', 'SAFT24kHz16BitMono',
    'eLEXTYPE_RESERVED4', 'DISPID_SGRsFindRule', 'SGRSTTDictation',
    'ISpeechLexiconWord', 'ISpPhrase', 'SpeechStreamFileMode',
    'DISPID_SRGRecoContext', 'DISPID_SWFEBitsPerSample',
    'SpeechTokenContext', 'DISPID_SVStatus',
    'SAFTCCITT_ALaw_8kHzMono', 'SpAudioFormat', 'SPPROPERTYINFO',
    'DISPID_SPCLangId', 'ISpeechLexicon',
    'SPSMF_SRGS_SEMANTICINTERPRETATION_W3C',
    'SAFTCCITT_ALaw_11kHzStereo', 'SAFTCCITT_uLaw_22kHzStereo',
    'DISPID_SASCurrentSeekPosition', 'SBOPause', 'SPSMF_UPS',
    'DISPID_SPIRule', 'SREPropertyNumChange', 'DISPID_SAFGuid',
    'DISPID_SPEPronunciation', 'SVSFUnusedFlags', 'SPEI_RECOGNITION',
    'SpeechRegistryUserRoot', 'DISPID_SRCState',
    'DISPID_SAFGetWaveFormatEx',
    'SpeechPropertyNormalConfidenceThreshold', 'SVESentenceBoundary',
    'SPSERIALIZEDPHRASE', 'DISPID_SRCCmdMaxAlternates',
    'DISPID_SLPsCount', 'ISpeechBaseStream', 'eWORDTYPE_DELETED',
    'SPRST_NUM_STATES', 'DISPID_SRCERecognitionForOtherContext',
    'SPWORD', 'ISpeechPhraseProperty', 'SDTDisplayText',
    'SPEI_RESERVED6', 'SPEI_SR_RETAINEDAUDIO', 'SPEI_MAX_TTS',
    'DISPID_SRSCurrentStreamPosition', 'DISPID_SpeechDataKey',
    'SPRECORESULTTIMES', 'DISPID_SOTsCount',
    'ISpeechGrammarRuleStateTransition', 'DISPID_SVEEnginePrivate',
    'DISPID_SPIReplacements', 'SAFTCCITT_uLaw_44kHzMono',
    'SpeechRecognizerState', 'SRERecognition', 'ISpRecoCategory',
    'DISPID_SPIGetDisplayAttributes', 'DISPID_SRCBookmark',
    'SPWORDLIST', 'SPRECOSTATE', 'SDKLCurrentConfig',
    'DISPID_SPEAudioSizeTime', 'DISPID_SGRSTsItem', 'SPSHT_OTHER',
    'ISpeechRecognizer', 'SP_VISEME_4', 'SPSUnknown',
    'DISPID_SRGCmdSetRuleIdState', 'DISPID_SGRSTPropertyValue',
    'IStream', 'DISPID_SpeechRecoResultTimes', 'eLEXTYPE_PRIVATE6',
    'SpeechVisemeType', 'SPEI_TTS_AUDIO_LEVEL', 'STSF_AppData',
    'DISPID_SPRuleEngineConfidence',
    'ISpeechGrammarRuleStateTransitions', 'SWTAdded',
    'SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE', 'SVEBookmark',
    'SRTAutopause', 'SAFTCCITT_uLaw_11kHzMono',
    'DISPID_SRRAlternates', 'SpeechRecoContextState', 'SPAS_RUN',
    'SPPS_Modifier', 'SRSEDone', 'SpeechCategoryAppLexicons',
    'SECFIgnoreKanaType', 'SPWT_LEXICAL_NO_SPECIAL_CHARS',
    'SPPHRASEPROPERTY', 'DISPID_SBSSeek', 'tagSPTEXTSELECTIONINFO',
    'SPEI_SENTENCE_BOUNDARY', 'SGDisplay',
    'DISPID_SRAllowAudioInputFormatChangesOnNextSet',
    'SPRST_INACTIVE_WITH_PURGE', 'DISPID_SPRDisplayAttributes',
    'SAFTGSM610_22kHzMono', 'SGRSTTWildcard', 'SPGS_ENABLED',
    'DISPID_SGRs_NewEnum', 'SPAS_CLOSED', 'DISPID_SLPsItem',
    'SPFM_CREATE_ALWAYS', 'DISPID_SPPBRestorePhraseFromMemory',
    'SpeechAudioFormatGUIDText', 'SPRS_ACTIVE',
    'DISPID_SVAudioOutput', 'SSTTTextBuffer', 'SPSTREAMFORMATTYPE',
    'SPEI_END_INPUT_STREAM', 'DISPID_SDKEnumValues', 'SPPHRASERULE',
    'SREFalseRecognition', 'DISPID_SOTDataKey', 'SRADefaultToActive',
    'ISpRecoGrammar', 'DISPID_SRGReset', 'SPPS_RESERVED4',
    'ISpNotifySource', 'DISPID_SLWType', 'SAFTNonStandardFormat',
    'SAFTADPCM_11kHzStereo', 'SDKLCurrentUser', 'DISPID_SASetState',
    'SASClosed', 'SPEI_VISEME', 'SAFT12kHz8BitMono',
    'DISPID_SGRsCommitAndSave', 'SPAR_High', '_SPAUDIOSTATE',
    'eLEXTYPE_PRIVATE15', 'SPSVerb', 'DISPID_SGRSTsCount',
    'ISpRecoContext', 'eLEXTYPE_PRIVATE10',
    'DISPID_SpeechPhraseBuilder', 'SAFTGSM610_8kHzMono',
    'ISpShortcut', 'SPEI_RESERVED5', 'SECFIgnoreWidth',
    'SPTEXTSELECTIONINFO', 'DISPID_SABufferInfo',
    'ISpNotifyTranslator', 'DISPID_SGRsAdd', 'SpeechRunState',
    'DISPID_SpeechLexiconProns', 'SPCT_SUB_COMMAND',
    'DISPID_SVSVisemeId', 'DISPIDSPTSI',
    'DISPID_SPRuleNumberOfElements', 'tagSPPROPERTYINFO', 'SPXRO_SML',
    'SAFTADPCM_11kHzMono', 'DISPID_SRRecognizer',
    'SWPUnknownWordPronounceable', 'DISPID_SRCRecognizer',
    'SPEI_REQUEST_UI', 'SVP_9', 'DISPID_SPEDisplayAttributes',
    'STCAll', 'DISPID_SPEEngineConfidence', 'SPDATAKEYLOCATION',
    'SPDKL_DefaultLocation', 'SPVPRI_NORMAL',
    'DISPID_SRCERecognizerStateChange',
    'DISPID_SpeechPhraseReplacement', 'DISPID_SVWaitUntilDone',
    'IEnumSpObjectTokens', 'SGDSActiveUserDelimited', 'SPAO_NONE',
    'SAFTCCITT_ALaw_22kHzStereo', 'DISPID_SVGetAudioInputs',
    'DISPID_SRGDictationUnload', 'SpResourceManager',
    'SpeechRecoProfileProperties', 'SPPS_RESERVED2',
    'SPEI_END_SR_STREAM', 'SREPropertyStringChange',
    'ISpeechVoiceStatus', 'SpMMAudioOut', 'SRAExport',
    'DISPID_SpeechLexiconWords', 'ISpRecognizer3', 'Library',
    '__MIDL___MIDL_itf_sapi_0000_0020_0001',
    'IInternetSecurityManager', 'ISpeechRecoResultTimes',
    'DISPID_SpeechAudioBufferInfo', 'SPEI_PROPERTY_NUM_CHANGE',
    'SGLexical', 'SAFTGSM610_44kHzMono', 'DISPID_SPEAudioTimeOffset',
    'SPRST_ACTIVE', 'SPCS_DISABLED', 'SITooQuiet',
    'DISPID_SASNonBlockingIO', 'ISpeechLexiconWords',
    'SpTextSelectionInformation', 'DISPID_SPARecoResult',
    'DISPID_SPRNumberOfElements', 'SAFTADPCM_44kHzMono',
    'DISPID_SRCVoice', 'SPRULE', 'ISpRecognizer', 'SRARoot',
    'DISPID_SRGetPropertyNumber', 'SPINTERFERENCE_NOSIGNAL',
    'eLEXTYPE_PRIVATE14', 'DISPID_SOTIsUISupported',
    'SPWAVEFORMATTYPE', 'SVP_19', 'ISpRecoResult',
    'DISPID_SpeechMemoryStream', 'SINoSignal',
    'SPEI_RECO_OTHER_CONTEXT', 'SPSHORTCUTPAIR', 'DISPID_SLWsCount',
    'ISpObjectTokenCategory', 'SPPHRASEREPLACEMENT',
    'SAFT16kHz16BitMono', 'SPINTERFERENCE_NOISE',
    'DISPID_SRCRetainedAudio', 'DISPID_SPAsItem',
    'DISPID_SDKDeleteKey', 'SAFTADPCM_8kHzStereo', 'DISPID_SRProfile',
    'SBONone', 'DISPID_SVGetProfiles', 'SVEPrivate',
    'SSFMCreateForWrite', 'SPINTERFERENCE_TOOSLOW', 'SPSHORTCUTTYPE',
    'SpShortcut', 'SVPOver', 'DISPID_SRRAudio', 'SAFT32kHz8BitMono',
    'SVSFlagsAsync', 'eLEXTYPE_RESERVED6', 'SRTEmulated',
    'SpeechMicTraining', 'Speech_Max_Pron_Length',
    'SpeechPropertyComplexResponseSpeed', 'DISPID_SLGenerationId',
    'DISPID_SPIRetainedSizeBytes', 'ISpPhraseAlt',
    'DISPID_SRRTTickCount', 'SAFT16kHz8BitMono', 'SPBO_PAUSE',
    'SP_VISEME_6', 'DISPID_SPPEngineConfidence',
    'SPWORDPRONUNCIATION', 'eLEXTYPE_APP', 'SPPS_Interjection',
    'SPEVENTSOURCEINFO', 'SPINTERFERENCE_LATENCY_WARNING',
    'DISPID_SBSFormat', 'SRSInactiveWithPurge',
    'DISPID_SpeechRecoContext',
    'DISPID_SpeechGrammarRuleStateTransitions', 'SPWORDTYPE',
    'DISPID_SLRemovePronunciationByPhoneIds',
    'SAFTCCITT_ALaw_11kHzMono', 'DISPID_SVSInputWordPosition',
    'SVP_2', 'SpNotifyTranslator', 'DISPID_SRGCommit',
    'SRCS_Disabled', 'ISpLexicon',
    'DISPID_SRCAudioInInterferenceStatus', 'SP_VISEME_2',
    'ISpeechPhraseReplacements', 'SpMemoryStream',
    '__MIDL_IWinTypes_0009', 'SPLO_STATIC', 'DISPID_SPPName',
    'SVSFParseSsml', 'SPEI_SOUND_START', 'SPCT_DICTATION',
    'SVSFParseAutodetect', 'SAFTCCITT_uLaw_11kHzStereo',
    'ISpeechTextSelectionInformation', 'SVSFNLPSpeakPunc',
    'SPFM_OPEN_READONLY', 'SAFT32kHz16BitMono',
    'DISPID_SVAllowAudioOuputFormatChangesOnNextSet',
    'DISPID_SpeechAudioFormat', 'SVF_None',
    '_ISpeechRecoContextEvents', 'SpMMAudioEnum',
    'DISPID_SPERetainedStreamOffset', 'SASRun',
    'DISPID_SPRuleChildren', 'SPRS_ACTIVE_USER_DELIMITED',
    'DISPID_SRSetPropertyNumber', 'SpeechPropertyAdaptationOn',
    'SP_VISEME_9', 'SDTAlternates', 'DISPID_SOTDisplayUI',
    'DISPID_SpeechPhraseAlternates', 'SVP_1',
    'SPEI_PROPERTY_STRING_CHANGE', 'DISPID_SPAStartElementInResult',
    'SPPS_SuppressWord', 'DISPID_SAStatus', 'SPEVENTENUM',
    'SpeechWordPronounceable', 'SECFDefault', 'DISPID_SGRsCommit',
    'SWTDeleted', 'SREInterference', 'DISPID_SAVolume',
    'STCInprocServer', 'SAFTDefault', 'DISPID_SFSOpen',
    'DISPID_SVVolume', 'ISpEventSink', 'eLEXTYPE_PRIVATE7',
    'DISPID_SRCSetAdaptationData', 'DISPID_SGRAddResource',
    'DISPID_SVEVoiceChange', 'DISPID_SVSLastBookmarkId', 'LONG_PTR',
    'DISPID_SRGCmdLoadFromMemory', 'SpFileStream',
    'SAFTADPCM_8kHzMono', 'ISpeechRecoResult2', 'SPAUDIOSTATE',
    'DISPID_SpeechPhraseProperties', 'eLEXTYPE_LETTERTOSOUND',
    'DISPID_SGRSTransitions', 'DISPID_SpeechPhraseInfo',
    'DISPID_SVSkip', 'ISpStreamFormat', 'DISPID_SPILanguageId',
    'SpeechSpecialTransitionType', 'DISPID_SLWWord',
    'DISPID_SpeechPhraseRules', 'DISPID_SOTGetStorageFileName',
    'SAFT24kHz16BitStereo', 'DISPID_SPIGrammarId',
    'DISPID_SPEActualConfidence', 'SPEI_ADAPTATION',
    'DISPID_SPRulesItem', 'SpeechGrammarTagDictation', 'SVP_21',
    'ISpSerializeState', 'ISpStream', 'DISPID_SRSClsidEngine',
    'SSSPTRelativeToEnd', 'DISPID_SRGCmdLoadFromResource',
    'SREPhraseStart', 'DISPID_SpeechGrammarRule', 'SPSHT_Unknown',
    'DISPID_SPRText', 'SRTExtendableParse', 'DISPID_SPPChildren',
    'DISPID_SVDisplayUI', 'DISPID_SDKOpenKey', 'SPCONTEXTSTATE',
    'DISPID_SGRAddState', 'DISPID_SGRsItem', 'ISpeechRecoResult',
    'SVP_16', 'DISPID_SWFESamplesPerSec', 'SSTTDictation',
    'DISPID_SpeechRecognizer', 'SECLowConfidence',
    'DISPID_SPRuleName', 'SpCompressedLexicon', 'SECNormalConfidence',
    'DISPID_SPRulesCount', 'ISpeechPhraseRules', 'DISPID_SVSpeak',
    'DISPID_SPRuleFirstElement', 'SpeechTokenIdUserLexicon',
    'SGRSTTEpsilon', 'SPPS_RESERVED1',
    '__MIDL___MIDL_itf_sapi_0000_0020_0002', 'DISPID_SPPConfidence',
    'DISPID_SPRuleConfidence', 'DISPID_SLRemovePronunciation',
    'SAFTCCITT_uLaw_8kHzStereo', 'DISPID_SpeechLexiconPronunciation',
    'SPFILEMODE', 'SPEI_PHRASE_START', 'SPAR_Low', 'SVEVoiceChange',
    'DISPID_SVSLastBookmark', 'SAFT44kHz16BitStereo',
    'DISPID_SGRSTs_NewEnum', 'SPRECOCONTEXTSTATUS',
    'ISpeechPhraseInfo', 'DISPID_SADefaultFormat',
    'DISPID_SLPSymbolic', 'DISPID_SVSRunningState',
    'DISPID_SABufferNotifySize', 'SFTSREngine', 'DISPID_SGRSTRule',
    'SPBINARYGRAMMAR', 'DISPID_SRGDictationLoad', 'SRSEIsSpeaking',
    'SSSPTRelativeToCurrentPosition', 'SPPS_NotOverriden',
    'eLEXTYPE_PRIVATE8', 'SITooSlow', 'SREStateChange',
    'SECFEmulateResult', 'SpeechPropertyResourceUsage',
    'DISPID_SVIsUISupported', 'SVPAlert', 'DISPID_SWFEFormatTag',
    'DISPID_SRIsShared', 'DISPID_SGRsDynamic', 'DISPID_SPAsCount',
    'DISPID_SGRInitialState', 'SPSNoun', 'SASPause',
    'DISPID_SOTRemoveStorageFileName', 'SpeechCategoryRecognizers',
    'DISPID_SpeechVoiceEvent', 'SpeechUserTraining',
    'DISPID_SpeechWaveFormatEx', 'DISPID_SDKGetlongValue',
    'ISpeechLexiconPronunciations', 'SAFT11kHz8BitMono',
    'SPAUDIOOPTIONS', 'SP_VISEME_13', 'SGLexicalNoSpecialChars',
    'SPSFunction', 'SPEI_SR_BOOKMARK', 'SGPronounciation',
    'SPEI_RESERVED3', 'SPINTERFERENCE', 'DISPID_SPIAudioSizeTime',
    'SpeechVoiceCategoryTTSRate', 'SPAO_RETAIN_AUDIO', 'SVSFIsXML',
    'DISPID_SABIBufferSize', 'SpPhraseInfoBuilder',
    'DISPID_SRRTLength', 'SAFTADPCM_44kHzStereo', 'SREAudioLevel',
    'SpStream', 'DISPID_SPPsItem', 'DISPID_SLGetGenerationChange',
    'SDTAudio', 'DISPID_SRGSetWordSequenceData', 'SP_VISEME_1',
    'ISpeechRecoGrammar', 'SDA_One_Trailing_Space', 'SRESoundStart',
    'SVP_4', 'DISPID_SRDisplayUI', 'Speech_Default_Weight',
    'SAFT8kHz16BitMono', 'DISPID_SOTCEnumerateTokens',
    'DISPID_SMSALineId', 'DISPID_SRIsUISupported',
    'ISpeechLexiconPronunciation', 'SPRST_INACTIVE',
    'DISPID_SRRSetTextFeedback', 'SPPS_Noun', 'SITooLoud',
    'SREAdaptation', 'eLEXTYPE_MORPHOLOGY', 'SAFT11kHz16BitStereo',
    'SVP_13', 'SPVOICESTATUS', 'DISPID_SRGCmdLoadFromFile',
    'DISPID_SPPId', 'SASStop', 'ISpeechAudio',
    'DISPID_SRRGetXMLErrorInfo', 'SPVPRI_ALERT',
    'DISPID_SpeechPhoneConverter', 'SSFMOpenReadWrite',
    'SpPhoneticAlphabetConverter', 'ISpPhoneticAlphabetConverter',
    'DISPIDSPTSI_SelectionLength', 'SINone', 'DISPID_SWFEBlockAlign',
    'DISPID_SpeechBaseStream', '_ISpeechVoiceEvents',
    'SpeechEmulationCompareFlags', 'SAFT22kHz16BitMono',
    'DISPID_SRRTStreamTime', 'SAFTTrueSpeech_8kHz1BitMono',
    'eLEXTYPE_PRIVATE9', 'DISPID_SVEStreamStart', 'SDTProperty',
    'eLEXTYPE_RESERVED10', 'SDTRule', 'SAFT24kHz8BitStereo',
    'ISpeechPhoneConverter', 'SAFTCCITT_uLaw_44kHzStereo',
    'DISPID_SRSAudioStatus', 'SECFNoSpecialChars',
    'eLEXTYPE_PRIVATE1', 'DISPID_SRGIsPronounceable', 'SP_VISEME_8',
    'SpeechGrammarState', 'SRSActive', 'SpeechLexiconType',
    'SpeechFormatType', 'SPPS_Noncontent', 'SAFT22kHz8BitMono',
    'SpeechGrammarTagUnlimitedDictation',
    'DISPID_SPPNumberOfElements', 'ISpeechResourceLoader',
    'STSF_CommonAppData', 'DISPID_SpeechGrammarRules',
    'SpeechStreamSeekPositionType', 'SPSNotOverriden', 'tagSTATSTG',
    'SPEI_START_INPUT_STREAM', 'DISPID_SREmulateRecognition',
    'SSFMOpenForRead', 'SpeechVoiceSpeakFlags',
    'DISPID_SpeechGrammarRuleState', 'SpObjectTokenCategory',
    'DISPID_SRCCreateGrammar', 'DISPID_SpeechRecognizerStatus',
    'DISPID_SPRuleParent', 'DISPID_SRRPhraseInfo',
    'DISPID_SRSCurrentStreamNumber', 'DISPID_SVEventInterests',
    'SREHypothesis', 'SGRSTTWord', 'DISPID_SOTCDefault',
    'SpeechCategoryVoices', 'SREAllEvents', 'eLEXTYPE_RESERVED8',
    'SSTTWildcard', 'SPAR_Medium', 'ISpeechAudioStatus',
    'SPWF_SRENGINE', 'DISPID_SLGetWords', 'SpeechAudioProperties',
    'DISPID_SGRId', 'DISPID_SDKGetStringValue', 'ISpPhoneConverter',
    'DISPID_SMSSetData', 'SpeechRuleState', 'SRADynamic',
    'SP_VISEME_19', 'SDKLDefaultLocation', 'SVSFParseSapi',
    'SPSModifier', 'SpeechInterference', 'SRCS_Enabled',
    'ISpeechRecoResultDispatch', 'SPAR_Unknown', 'SPEI_SR_PRIVATE',
    'SECHighConfidence', 'SpSharedRecognizer',
    'SpeechCategoryPhoneConverters', 'DISPID_SAEventHandle',
    'eLEXTYPE_PRIVATE12', 'SAFT12kHz16BitMono', 'SPBO_NONE',
    'DISPID_SpeechPhraseProperty', 'SINoise', 'DISPID_SVResume',
    'DISPID_SGRSRule', 'SVP_20', 'ISpeechPhraseAlternates',
    'ISpeechMMSysAudio', 'SpeechLoadOption', 'SRAInterpreter',
    'DISPID_SRCEBookmark', 'SVP_8', 'DISPIDSPTSI_ActiveLength',
    'Speech_StreamPos_RealTime', 'DISPID_SCSBaseStream',
    'DISPID_SPIEngineId', 'DISPID_SRCERecognition', 'SPEI_RESERVED1',
    'SP_VISEME_21', 'DISPID_SRGCmdSetRuleState',
    'DISPID_SpeechGrammarRuleStateTransition', 'SRSInactive',
    'DISPID_SOTCGetDataKey', 'STCLocalServer', 'SVP_10',
    'IEnumString', 'DISPID_SPIAudioSizeBytes',
    'DISPID_SPEDisplayText', 'SLTApp', 'ISpPhoneticAlphabetSelection',
    'SPSMF_SRGS_SEMANTICINTERPRETATION_MS', 'SPPHRASEELEMENT',
    'SDA_Two_Trailing_Spaces', 'SAFTExtendedAudioFormat',
    'DISPID_SPCIdToPhone', 'SAFT12kHz8BitStereo', 'DISPID_SAFType',
    'DISPID_SPIEnginePrivateData', 'ISpeechObjectToken',
    'SPBOOKMARKOPTIONS', 'ISpeechXMLRecoResult', 'SPRULESTATE',
    'SRAONone', 'SVSFPersistXML', 'ISpObjectToken', 'SFTInput',
    'DISPID_SDKDeleteValue', 'DISPID_SRRAudioFormat',
    'DISPID_SWFEChannels', 'DISPID_SRGSetTextSelection',
    'DISPID_SMSADeviceId', 'SPSHT_NotOverriden', 'SGRSTTTextBuffer',
    'eLEXTYPE_PRIVATE2', 'SpeechGrammarRuleStateTransitionType',
    'STSF_FlagCreate', 'ISpeechObjectTokenCategory', 'SDTAll',
    'SPEI_WORD_BOUNDARY', 'DISPID_SVRate', 'SSFMCreate',
    'DISPID_SpeechCustomStream', 'SVPNormal',
    'DISPID_SLPPartOfSpeech', 'DISPID_SVSInputSentenceLength',
    'SREStreamStart', 'SPBO_AHEAD', 'DISPID_SPRs_NewEnum',
    'DISPID_SVGetAudioOutputs', 'DISPID_SRRRecoContext',
    'SAFT16kHz8BitStereo', 'DISPID_SpeechVoiceStatus',
    'DISPID_SVEBookmark', 'WAVEFORMATEX', 'SAFT8kHz16BitStereo',
    'SAFT11kHz16BitMono', 'DISPID_SRSetPropertyString',
    'SVEWordBoundary', 'DISPID_SPAs_NewEnum',
    'ISpeechPhraseReplacement', 'SVSFNLPMask',
    'SWPUnknownWordUnpronounceable', 'DISPID_SVSCurrentStreamNumber',
    'SPINTERFERENCE_TOOQUIET', 'DISPID_SRCreateRecoContext',
    'DISPID_SRRTOffsetFromStart', 'DISPID_SOTId',
    'ISpeechPhraseElement', 'SAFT22kHz8BitStereo', 'SVSFVoiceMask',
    'SP_VISEME_15', 'SPEI_RECO_STATE_CHANGE', 'SPSLMA',
    'SPEI_START_SR_STREAM', 'SpCustomStream',
    'DISPID_SpeechMMSysAudio', 'SSSPTRelativeToStart',
    'SDKLLocalMachine', 'SPDKL_CurrentUser', 'SpeechAddRemoveWord',
    'SPPARTOFSPEECH', 'DISPID_SPIGetText', 'DISPID_SPPValue',
    'SPINTERFERENCE_NONE', 'ISpeechAudioFormat', 'SREPrivate',
    'DISPID_SPPs_NewEnum', 'SVP_7', 'SpeechEngineProperties',
    'SPBO_TIME_UNITS', 'DISPID_SRCEEndStream', 'ISpMMSysAudio',
    'SPWORDPRONUNCIATIONLIST', 'SpeechAudioFormatGUIDWave',
    'SAFTCCITT_ALaw_8kHzStereo', 'DISPID_SGRAttributes',
    'DISPID_SMSAMMHandle', 'eLEXTYPE_PRIVATE19',
    'DISPID_SpeechObjectTokens', 'SLTUser', 'SREBookmark',
    'DISPID_SpeechRecoContextEvents', 'SpeechPartOfSpeech',
    'eLEXTYPE_PRIVATE5', 'DISPID_SLPPhoneIds', 'DISPID_SPEs_NewEnum',
    'DISPID_SOTMatchesAttributes', 'SAFTCCITT_ALaw_22kHzMono',
    'SAFTText', 'SDA_No_Trailing_Space', 'SPSHORTCUTPAIRLIST',
    'DISPID_SRAudioInput', 'SPLEXICONTYPE', 'DISPID_SRRGetXMLResult',
    'SVSFIsNotXML', 'SPFM_OPEN_READWRITE', '_RemotableHandle',
    'eLEXTYPE_VENDORLEXICON', 'DISPID_SVSpeakCompleteEvent',
    'DISPID_SPRules_NewEnum', 'SP_VISEME_5', 'SP_VISEME_12',
    'DISPID_SBSRead', 'SpeechVoiceSkipTypeSentence',
    'DISPID_SPAPhraseInfo', 'SPEI_TTS_BOOKMARK',
    'DISPID_SpeechRecoResult', 'DISPID_SABIEventBias',
    'DISPID_SRRDiscardResultInfo', 'SpeechRecoEvents',
    'DISPID_SRRSpeakAudio', 'SPAUDIOSTATUS',
    'DISPID_SPERetainedSizeBytes', 'DISPIDSPTSI_SelectionOffset',
    'SPRST_ACTIVE_ALWAYS', 'SITooFast', 'SpeechTokenKeyUI',
    'ISpDataKey', 'DISPID_SRGId', 'SpObjectToken', 'SP_VISEME_17',
    'SpeechDisplayAttributes', 'SAFT48kHz16BitMono',
    'DISPID_SRGRules', 'SAFT12kHz16BitStereo', 'SpeechVisemeFeature',
    'SDTReplacement', 'SDTLexicalForm', 'DISPID_SPEAudioStreamOffset',
    'SpeechPropertyHighConfidenceThreshold',
    'ISpStreamFormatConverter', 'SPWP_UNKNOWN_WORD_PRONOUNCEABLE',
    'DISPID_SRCResume', 'SGDSInactive', 'SVP_18', 'DISPID_SRCPause',
    'DISPID_SRCEPropertyStringChange', 'SpeechTokenValueCLSID',
    'DISPID_SLPs_NewEnum', 'DISPID_SPPParent',
    'DISPID_SPELexicalForm', 'DISPID_SVEWord', 'SVP_0',
    'DISPID_SRCESoundEnd', 'DISPID_SRSNumberOfActiveRules',
    'SPVPRI_OVER', 'SP_VISEME_20', 'SPEI_SOUND_END',
    'SpeechEngineConfidence', 'SAFT32kHz16BitStereo',
    'SpInProcRecoContext', 'SVF_Emphasis',
    'SPRS_ACTIVE_WITH_AUTO_PAUSE', 'SpeechRecognitionType',
    'DISPID_SPPFirstElement', 'DISPID_SFSClose', 'SVP_5',
    'SPGRAMMARWORDTYPE', 'SpeechRuleAttributes',
    'ISpeechPhraseElements', 'SRESoundEnd',
    'DISPID_SVESentenceBoundary', 'typelib_path', 'SECFIgnoreCase',
    'DISPID_SPRuleId', 'DISPID_SLGetPronunciations',
    'DISPID_SpeechPhraseElements', 'DISPID_SOTsItem',
    'DISPID_SPCPhoneToId', 'DISPID_SLPLangId', 'SLODynamic',
    'SAFT44kHz8BitMono', 'eLEXTYPE_PRIVATE4',
    'DISPID_SRCEEnginePrivate', 'SP_VISEME_16', 'DISPID_SLWs_NewEnum',
    'ISpeechFileStream', 'SpeechAudioFormatType', 'SGRSTTRule',
    'DISPID_SPIStartTime', 'SRERecoOtherContext',
    'DISPID_SRCCreateResultFromMemory', 'SpUnCompressedLexicon',
    'DISPID_SpeechXMLRecoResult', 'eLEXTYPE_RESERVED7',
    'DISPID_SLPType', 'DISPID_SpeechFileStream', 'SRATopLevel',
    'DISPID_SpeechPhraseAlternate', 'DISPID_SGRSTType',
    'DISPID_SRState', 'SVEAllEvents', 'SP_VISEME_7',
    'DISPID_SDKGetBinaryValue', 'ISpeechDataKey', 'SRAORetainAudio',
    'SVP_11', 'SAFTCCITT_ALaw_44kHzStereo',
    'DISPID_SDKSetStringValue', 'DISPID_SRGDictationSetState',
    'DISPID_SRCEPhraseStart', 'ISpVoice',
    'SPWP_KNOWN_WORD_PRONOUNCEABLE', 'SVP_14', 'SPEI_VOICE_CHANGE',
    'SPPS_Verb', 'SPSInterjection', 'DISPID_SVSLastResult',
    'DISPID_SRCEHypothesis', 'ISpeechGrammarRuleState',
    'DISPID_SPIElements', 'DISPID_SLAddPronunciation',
    'DISPID_SRStatus', 'SpeechAudioState', 'DISPID_SDKSetLongValue',
    'SAFT8kHz8BitStereo', 'ISpeechPhraseAlternate',
    'SpeechCategoryRecoProfiles', 'SP_VISEME_10',
    'SDA_Consume_Leading_Spaces', 'SP_VISEME_14', 'SVF_Stressed',
    'ISpRecognizer2', 'ISpeechPhraseInfoBuilder',
    'DISPID_SVAlertBoundary', 'ISpeechRecognizerStatus',
    'SAFT44kHz16BitMono', 'SpLexicon', 'SPSEMANTICFORMAT',
    'DISPID_SRCEventInterests', 'DISPID_SOTRemove',
    'DISPID_SMSGetData', 'DISPID_SVSPhonemeId', 'SREStreamEnd',
    'DISPID_SRRTimes', 'SpeechTokenKeyAttributes',
    'DISPID_SOTCategory', 'SPEI_TTS_PRIVATE', 'DISPID_SPRsCount',
    'DISPID_SASState', 'eLEXTYPE_USER_SHORTCUT', 'eLEXTYPE_PRIVATE13',
    'DISPID_SPANumberOfElementsInResult', 'SVSFDefault',
    'SDTPronunciation', 'DISPID_SPEAudioSizeBytes',
    'SAFTNoAssignedFormat', 'DISPID_SRCEAudioLevel', 'SPCS_ENABLED',
    'SP_VISEME_0', 'DISPID_SRCEInterference', 'SPEI_SR_AUDIO_LEVEL',
    'SAFT24kHz8BitMono', 'SPAS_PAUSE', 'SPEI_MAX_SR', 'SRTReSent',
    'SPEI_FALSE_RECOGNITION', 'SP_VISEME_11',
    'DISPID_SOTCreateInstance', 'DISPID_SRGState', 'SAFT8kHz8BitMono',
    'DISPID_SLWPronunciations', 'SRAImport', 'DISPID_SRCERequestUI',
    'DISPID_SGRSAddSpecialTransition', 'SpeechTokenKeyFiles',
    'SpeechAudioVolume', 'DISPID_SWFEExtraData', 'DISPID_SOTSetId',
    'SPLOADOPTIONS', 'SpPhoneConverter', 'ISpeechRecoContext',
    'SPINTERFERENCE_TOOFAST', 'DISPID_SRCEStartStream',
    'SpeechWordType', 'SAFT22kHz16BitStereo', 'DISPID_SGRName',
    'SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN', 'DISPID_SVPriority',
    'SpeechDiscardType', 'SPDKL_CurrentConfig', 'SPFM_CREATE',
    'SVSFIsFilename', 'DISPID_SpeechPhraseReplacements',
    'ISpeechCustomStream', 'SVEViseme', 'DISPID_SRAudioInputStream',
    'SPEI_UNDEFINED', 'SPPS_RESERVED3', 'DISPID_SPRFirstElement',
    'DISPID_SpeechAudio', 'eLEXTYPE_RESERVED9',
    'DISPID_SRCESoundStart', 'SPEI_INTERFERENCE', 'SPWT_DISPLAY',
    'SGSEnabled', 'ISpeechWaveFormatEx', 'SPSEMANTICERRORINFO',
    'ISpeechPhraseProperties', 'SRERequestUI', 'SPAUDIOBUFFERINFO',
    'DISPIDSPTSI_ActiveOffset', 'DISPID_SDKEnumKeys', 'ISpNotifySink',
    'DISPID_SABIMinNotification', 'DISPID_SASCurrentDevicePosition',
    'DISPID_SVEViseme', 'SPWT_PRONUNCIATION', 'STSF_LocalAppData',
    'DISPID_SPIAudioStreamPosition', 'eLEXTYPE_PRIVATE17',
    'SpeechVoiceEvents', 'SPSERIALIZEDRESULT',
    'DISPID_SVSyncronousSpeakTimeout', 'eLEXTYPE_PRIVATE11',
    'SpeechDataKeyLocation', 'SPVPRIORITY', 'ISpRecoGrammar2',
    'ISpGrammarBuilder', 'SPGS_EXCLUSIVE',
    'SpeechRegistryLocalMachineRoot', 'DISPID_SRGetFormat',
    'DISPID_SGRSTPropertyId', 'ISpeechMemoryStream',
    'DISPID_SpeechObjectTokenCategory', 'DISPID_SVVoice',
    'eLEXTYPE_PRIVATE20', 'Speech_StreamPos_Asap', 'SpMMAudioIn',
    'DISPID_SGRSAddWordTransition', 'SRTStandard', 'SRSActiveAlways',
    'SpInprocRecognizer', 'SPEI_PHONEME',
    'DISPID_SRCEFalseRecognition', 'SpStreamFormatConverter',
    'Speech_Max_Word_Length', 'DISPID_SpeechPhraseRule',
    'DISPID_SOTCSetId', 'ISpeechVoice', 'DISPID_SpeechObjectToken',
    'DISPID_SRGetRecognizers', 'eLEXTYPE_PRIVATE16',
    'SpeechPropertyLowConfidenceThreshold', 'DISPIDSPRG',
    'DISPID_SWFEAvgBytesPerSec', 'SGDSActive', 'SVEAudioLevel',
    'SPEI_MIN_SR', 'DISPID_SAFSetWaveFormatEx',
    'DISPID_SPISaveToMemory', 'SPEI_HYPOTHESIS',
    'SAFT11kHz8BitStereo', 'STCRemoteServer', 'SPRS_INACTIVE',
    'SPSMF_SRGS_SAPIPROPERTIES', 'SPXRO_Alternates_SML',
    'SRTSMLTimeout', 'ISpXMLRecoResult', 'SPEI_MIN_TTS',
    'SAFT32kHz8BitStereo', 'SAFT44kHz8BitStereo',
    'SAFTADPCM_22kHzStereo',
    'DISPID_SRAllowVoiceFormatMatchingOnNextSet',
    'DISPID_SRCVoicePurgeEvent', 'SpNullPhoneConverter',
    'ISpObjectWithToken', 'SAFTADPCM_22kHzMono', 'SVEEndInputStream',
    'SVEStartInputStream', 'DISPID_SASFreeBufferSpace',
    'SPWORDPRONOUNCEABLE', 'SPXMLRESULTOPTIONS',
    'SpeechCategoryAudioIn', 'SpeechDictationTopicSpelling',
    'SAFT48kHz16BitStereo', 'SPCT_SLEEP',
    'DISPID_SVSInputSentencePosition', 'SVP_6',
    'DISPID_SRCRequestedUIType'
]

