/home/nicommartinez2002/thau012/NICOLAS MARTINEZ MARTINEZ PHD/AÑO 1/NUEVA ARQ/CANARY1B-V2/arq_kernels
├── agents
│   ├── __init__.py
│   └── voice_agent
│       ├── __init__.py
│       ├── pipecat
│       │   ├── frames
│       │   │   ├── frames.py
│       │   │   └── __init__.py
│       │   ├── __init__.py
│       │   ├── processors
│       │   │   ├── frameworks
│       │   │   │   ├── __init__.py
│       │   │   │   └── rtvi.py
│       │   │   └── __init__.py
│       │   ├── services
│       │   │   ├── __init__.py
│       │   │   └── nemo
│       │   │       ├── audio_logger.py
│       │   │       ├── diar.py
│       │   │       ├── __init__.py
│       │   │       ├── llm.py
│       │   │       ├── streaming_asr.py
│       │   │       ├── streaming_diar.py
│       │   │       ├── stt.py
│       │   │       ├── tts.py
│       │   │       ├── turn_taking.py
│       │   │       └── utils.py
│       │   ├── transports
│       │   │   ├── base_input.py
│       │   │   ├── base_transport.py
│       │   │   ├── __init__.py
│       │   │   └── network
│       │   │       ├── __init__.py
│       │   │       └── websocket_server.py
│       │   └── utils
│       │       ├── __init__.py
│       │       ├── text
│       │       │   ├── __init__.py
│       │       │   └── simple_text_aggregator.py
│       │       └── tool_calling
│       │           ├── basic_tools.py
│       │           ├── __init__.py
│       │           └── mixins.py
│       └── utils
│           ├── config_manager.py
│           └── __init__.py
├── collections
│   ├── asr
│   │   ├── data
│   │   │   ├── audio_to_ctm_dataset.py
│   │   │   ├── audio_to_diar_label_lhotse.py
│   │   │   ├── audio_to_diar_label.py
│   │   │   ├── audio_to_label_dataset.py
│   │   │   ├── audio_to_label.py
│   │   │   ├── audio_to_text_dali.py
│   │   │   ├── audio_to_text_dataset.py
│   │   │   ├── audio_to_text_lhotse_prompted.py
│   │   │   ├── audio_to_text_lhotse_prompt.py
│   │   │   ├── audio_to_text_lhotse.py
│   │   │   ├── audio_to_text_lhotse_speaker.py
│   │   │   ├── audio_to_text.py
│   │   │   ├── data_simulation.py
│   │   │   ├── feature_to_label_dataset.py
│   │   │   ├── feature_to_label.py
│   │   │   ├── feature_to_text_dataset.py
│   │   │   ├── feature_to_text.py
│   │   │   ├── huggingface
│   │   │   │   ├── hf_audio_to_text_dataset.py
│   │   │   │   ├── hf_audio_to_text.py
│   │   │   │   └── __init__.py
│   │   │   ├── __init__.py
│   │   │   ├── ssl_dataset.py
│   │   │   └── text_to_text.py
│   │   ├── inference
│   │   │   ├── factory
│   │   │   │   ├── base_builder.py
│   │   │   │   ├── buffered_pipeline_builder.py
│   │   │   │   ├── cache_aware_pipeline_builder.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── pipeline_builder.py
│   │   │   ├── __init__.py
│   │   │   ├── itn
│   │   │   │   ├── batch_inverse_normalizer.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── inverse_normalizer.py
│   │   │   ├── model_wrappers
│   │   │   │   ├── asr_inference_wrapper.py
│   │   │   │   ├── cache_aware_asr_inference_wrapper.py
│   │   │   │   ├── cache_aware_ctc_inference_wrapper.py
│   │   │   │   ├── cache_aware_rnnt_inference_wrapper.py
│   │   │   │   ├── ctc_inference_wrapper.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── rnnt_inference_wrapper.py
│   │   │   ├── nmt
│   │   │   │   ├── __init__.py
│   │   │   │   ├── llm_translator.py
│   │   │   │   └── prompts.py
│   │   │   ├── pipelines
│   │   │   │   ├── base_pipeline.py
│   │   │   │   ├── buffered_ctc_pipeline.py
│   │   │   │   ├── buffered_rnnt_pipeline.py
│   │   │   │   ├── cache_aware_ctc_pipeline.py
│   │   │   │   ├── cache_aware_rnnt_pipeline.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── pipeline_interface.py
│   │   │   ├── streaming
│   │   │   │   ├── buffering
│   │   │   │   │   ├── audio_bufferer.py
│   │   │   │   │   ├── cache_feature_bufferer.py
│   │   │   │   │   ├── feature_bufferer.py
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── decoders
│   │   │   │   │   ├── greedy
│   │   │   │   │   │   ├── greedy_ctc_decoder.py
│   │   │   │   │   │   ├── greedy_decoder.py
│   │   │   │   │   │   ├── greedy_rnnt_decoder.py
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── endpointing
│   │   │   │   │   ├── greedy
│   │   │   │   │   │   ├── greedy_ctc_endpointing.py
│   │   │   │   │   │   ├── greedy_endpointing.py
│   │   │   │   │   │   ├── greedy_rnnt_endpointing.py
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── framing
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── mono_stream.py
│   │   │   │   │   ├── multi_stream.py
│   │   │   │   │   ├── request_options.py
│   │   │   │   │   ├── request.py
│   │   │   │   │   └── stream.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── state
│   │   │   │   │   ├── cache_aware_ctc_state.py
│   │   │   │   │   ├── cache_aware_rnnt_state.py
│   │   │   │   │   ├── cache_aware_state.py
│   │   │   │   │   ├── ctc_state.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── rnnt_state.py
│   │   │   │   │   └── state.py
│   │   │   │   └── text
│   │   │   │       ├── __init__.py
│   │   │   │       └── text_processing.py
│   │   │   └── utils
│   │   │       ├── audio_io.py
│   │   │       ├── bpe_decoder.py
│   │   │       ├── config_io.py
│   │   │       ├── constants.py
│   │   │       ├── context_manager.py
│   │   │       ├── device_utils.py
│   │   │       ├── endpointing_utils.py
│   │   │       ├── enums.py
│   │   │       ├── __init__.py
│   │   │       ├── itn_utils.py
│   │   │       ├── manifest_io.py
│   │   │       ├── pipeline_eval.py
│   │   │       ├── pipeline_utils.py
│   │   │       ├── progressbar.py
│   │   │       ├── state_management_utils.py
│   │   │       └── text_segment.py
│   │   ├── __init__.py
│   │   ├── losses
│   │   │   ├── angularloss.py
│   │   │   ├── bce_loss.py
│   │   │   ├── ctc.py
│   │   │   ├── __init__.py
│   │   │   ├── lattice_losses.py
│   │   │   ├── rnnt.py
│   │   │   ├── rnnt_pytorch.py
│   │   │   └── ssl_losses
│   │   │       ├── contrastive.py
│   │   │       ├── ctc.py
│   │   │       ├── __init__.py
│   │   │       ├── mlm.py
│   │   │       └── rnnt.py
│   │   ├── metrics
│   │   │   ├── bleu.py
│   │   │   ├── der.py
│   │   │   ├── __init__.py
│   │   │   ├── multi_binary_acc.py
│   │   │   ├── multitask.py
│   │   │   └── wer.py
│   │   ├── models
│   │   │   ├── aed_multitask_models.py
│   │   │   ├── asr_model.py
│   │   │   ├── classification_models.py
│   │   │   ├── clustering_diarizer.py
│   │   │   ├── confidence_ensemble.py
│   │   │   ├── configs
│   │   │   │   ├── aligner_config.py
│   │   │   │   ├── asr_models_config.py
│   │   │   │   ├── classification_models_config.py
│   │   │   │   ├── diarizer_config.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── k2_sequence_models_config.py
│   │   │   │   ├── matchboxnet_config.py
│   │   │   │   └── quartznet_config.py
│   │   │   ├── ctc_bpe_models.py
│   │   │   ├── ctc_models.py
│   │   │   ├── hybrid_asr_tts_models.py
│   │   │   ├── hybrid_rnnt_ctc_bpe_models_prompt.py
│   │   │   ├── hybrid_rnnt_ctc_bpe_models.py
│   │   │   ├── hybrid_rnnt_ctc_models.py
│   │   │   ├── __init__.py
│   │   │   ├── k2_aligner_model.py
│   │   │   ├── k2_sequence_models.py
│   │   │   ├── label_models.py
│   │   │   ├── msdd_models.py
│   │   │   ├── multitalker_asr_models.py
│   │   │   ├── online_diarizer.py
│   │   │   ├── rnnt_bpe_models.py
│   │   │   ├── rnnt_models.py
│   │   │   ├── slu_models.py
│   │   │   ├── sortformer_diar_models.py
│   │   │   ├── ssl_models.py
│   │   │   └── transformer_bpe_models.py
│   │   ├── modules
│   │   │   ├── audio_preprocessing.py
│   │   │   ├── beam_search_decoder.py
│   │   │   ├── conformer_encoder.py
│   │   │   ├── conv_asr.py
│   │   │   ├── flashlight_decoder.py
│   │   │   ├── graph_decoder.py
│   │   │   ├── hybrid_autoregressive_transducer.py
│   │   │   ├── __init__.py
│   │   │   ├── lstm_decoder.py
│   │   │   ├── msdd_diarizer.py
│   │   │   ├── rnn_encoder.py
│   │   │   ├── rnnt_abstract.py
│   │   │   ├── rnnt.py
│   │   │   ├── sortformer_modules.py
│   │   │   ├── squeezeformer_encoder.py
│   │   │   ├── ssl_modules
│   │   │   │   ├── augmentation.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── masking.py
│   │   │   │   ├── multi_layer_feat.py
│   │   │   │   ├── multi_softmax_decoder.py
│   │   │   │   └── quantizers.py
│   │   │   ├── transformer
│   │   │   │   ├── bridge_encoders.py
│   │   │   │   ├── decoder_module.py
│   │   │   │   ├── encoder_module.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── perceiver_encoders.py
│   │   │   │   ├── reduction_encoders.py
│   │   │   │   ├── text_generation.py
│   │   │   │   ├── transformer_bottleneck.py
│   │   │   │   ├── transformer_decoders.py
│   │   │   │   ├── transformer_encoders_nlp.py
│   │   │   │   ├── transformer_encoders.py
│   │   │   │   ├── transformer_generators.py
│   │   │   │   ├── transformer_modules.py
│   │   │   │   ├── transformer.py
│   │   │   │   └── transformer_utils.py
│   │   │   └── wav2vec_modules.py
│   │   ├── parts
│   │   │   ├── context_biasing
│   │   │   │   ├── biasing_multi_model.py
│   │   │   │   ├── boosting_graph_batched.py
│   │   │   │   ├── context_biasing_utils.py
│   │   │   │   ├── context_graph_ctc.py
│   │   │   │   ├── context_graph_universal.py
│   │   │   │   ├── ctc_based_word_spotter.py
│   │   │   │   └── __init__.py
│   │   │   ├── features.py
│   │   │   ├── __init__.py
│   │   │   ├── k2
│   │   │   │   ├── classes.py
│   │   │   │   ├── grad_utils.py
│   │   │   │   ├── graph_compilers.py
│   │   │   │   ├── graph_decoders.py
│   │   │   │   ├── graph_transducer.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── loss_mixins.py
│   │   │   │   ├── map_loss.py
│   │   │   │   ├── ml_loss.py
│   │   │   │   ├── rnnt_logprobs.py
│   │   │   │   ├── rnnt_logprobs_triton.py
│   │   │   │   ├── topologies.py
│   │   │   │   ├── utils.py
│   │   │   │   └── w_transducer.py
│   │   │   ├── mixins
│   │   │   │   ├── asr_adapter_mixins.py
│   │   │   │   ├── diarization.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── interctc_mixin.py
│   │   │   │   ├── mixins.py
│   │   │   │   ├── multitalker_asr_mixins.py
│   │   │   │   ├── streaming.py
│   │   │   │   └── transcription.py
│   │   │   ├── numba
│   │   │   │   ├── __init__.py
│   │   │   │   ├── rnnt_loss
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── rnnt_numpy.py
│   │   │   │   │   ├── rnnt.py
│   │   │   │   │   ├── rnnt_pytorch.py
│   │   │   │   │   └── utils
│   │   │   │   │       ├── cpu_utils
│   │   │   │   │       │   ├── cpu_rnnt.py
│   │   │   │   │       │   └── __init__.py
│   │   │   │   │       ├── cuda_utils
│   │   │   │   │       │   ├── gpu_rnnt_kernel.py
│   │   │   │   │       │   ├── gpu_rnnt.py
│   │   │   │   │       │   ├── __init__.py
│   │   │   │   │       │   └── reduce.py
│   │   │   │   │       ├── global_constants.py
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       └── rnnt_helper.py
│   │   │   │   └── spec_augment
│   │   │   │       ├── __init__.py
│   │   │   │       └── spec_aug_numba.py
│   │   │   ├── preprocessing
│   │   │   │   ├── feature_loader.py
│   │   │   │   ├── features.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── perturb.py
│   │   │   │   └── segment.py
│   │   │   ├── submodules
│   │   │   │   ├── adapters
│   │   │   │   │   ├── attention_adapter_mixin.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── multi_head_attention_adapter_module.py
│   │   │   │   │   └── transformer_multi_head_attention_adapter_module.py
│   │   │   │   ├── aed_decoding
│   │   │   │   │   ├── aed_batched_streaming.py
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── batchnorm.py
│   │   │   │   ├── causal_convs.py
│   │   │   │   ├── classifier.py
│   │   │   │   ├── conformer_modules.py
│   │   │   │   ├── ctc_batched_beam_decoding.py
│   │   │   │   ├── ctc_beam_decoding.py
│   │   │   │   ├── ctc_decoding.py
│   │   │   │   ├── ctc_greedy_decoding.py
│   │   │   │   ├── cuda_graph_rnnt_greedy_decoding.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── jasper.py
│   │   │   │   ├── multi_head_attention.py
│   │   │   │   ├── multitask_beam_decoding.py
│   │   │   │   ├── multitask_decoding.py
│   │   │   │   ├── multitask_greedy_decoding.py
│   │   │   │   ├── ngram_lm
│   │   │   │   │   ├── constants.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── kenlm_utils.py
│   │   │   │   │   ├── ngram_lm_batched.py
│   │   │   │   │   └── ngram_lm_triton.py
│   │   │   │   ├── rnnt_beam_decoding.py
│   │   │   │   ├── rnnt_decoding.py
│   │   │   │   ├── rnnt_greedy_decoding.py
│   │   │   │   ├── rnnt_maes_batched_computer.py
│   │   │   │   ├── rnnt_malsd_batched_computer.py
│   │   │   │   ├── spectr_augment.py
│   │   │   │   ├── squeezeformer_modules.py
│   │   │   │   ├── ssl_quantizers.py
│   │   │   │   ├── stateless_net.py
│   │   │   │   ├── subsampling.py
│   │   │   │   ├── tdnn_attention.py
│   │   │   │   ├── tdt_beam_decoding.py
│   │   │   │   ├── tdt_malsd_batched_computer.py
│   │   │   │   ├── token_classifier.py
│   │   │   │   ├── transducer_decoding
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── label_looping_base.py
│   │   │   │   │   ├── rnnt_label_looping.py
│   │   │   │   │   └── tdt_label_looping.py
│   │   │   │   └── wfst_decoder.py
│   │   │   └── utils
│   │   │       ├── activations.py
│   │   │       ├── adapter_utils.py
│   │   │       ├── aligner_utils.py
│   │   │       ├── asr_batching.py
│   │   │       ├── asr_confidence_benchmarking_utils.py
│   │   │       ├── asr_confidence_utils.py
│   │   │       ├── asr_module_utils.py
│   │   │       ├── asr_multispeaker_utils.py
│   │   │       ├── batched_beam_decoding_utils.py
│   │   │       ├── chunking_utils.py
│   │   │       ├── confidence_metrics.py
│   │   │       ├── data_simulation_utils.py
│   │   │       ├── decoder_timestamps_utils.py
│   │   │       ├── diarization_utils.py
│   │   │       ├── eval_utils.py
│   │   │       ├── __init__.py
│   │   │       ├── longform_clustering.py
│   │   │       ├── manifest_utils.py
│   │   │       ├── multispk_transcribe_utils.py
│   │   │       ├── numba_utils.py
│   │   │       ├── offline_clustering.py
│   │   │       ├── online_clustering.py
│   │   │       ├── optimization_utils.py
│   │   │       ├── regularization_utils.py
│   │   │       ├── rnnt_utils.py
│   │   │       ├── slu_utils.py
│   │   │       ├── speaker_utils.py
│   │   │       ├── streaming_utils.py
│   │   │       ├── timestamp_utils.py
│   │   │       ├── tokenizer_utils.py
│   │   │       ├── transcribe_utils.py
│   │   │       ├── vad_utils.py
│   │   │       └── wfst_utils.py
│   │   └── README.md
│   ├── audio
│   │   ├── data
│   │   │   ├── audio_to_audio_dataset.py
│   │   │   ├── audio_to_audio_lhotse.py
│   │   │   ├── audio_to_audio.py
│   │   │   ├── data_simulation.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── losses
│   │   │   ├── audio.py
│   │   │   ├── __init__.py
│   │   │   └── maxine
│   │   │       ├── __init__.py
│   │   │       ├── losses_combined.py
│   │   │       └── sisnr_loss.py
│   │   ├── metrics
│   │   │   ├── audio.py
│   │   │   ├── __init__.py
│   │   │   └── squim.py
│   │   ├── models
│   │   │   ├── audio_to_audio.py
│   │   │   ├── enhancement.py
│   │   │   ├── __init__.py
│   │   │   └── maxine
│   │   │       ├── bnr.py
│   │   │       └── __init__.py
│   │   ├── modules
│   │   │   ├── features.py
│   │   │   ├── __init__.py
│   │   │   ├── masking.py
│   │   │   ├── projections.py
│   │   │   ├── ssl_pretrain_masking.py
│   │   │   └── transforms.py
│   │   ├── parts
│   │   │   ├── __init__.py
│   │   │   ├── submodules
│   │   │   │   ├── conformer.py
│   │   │   │   ├── conformer_unet.py
│   │   │   │   ├── diffusion.py
│   │   │   │   ├── flow.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── multichannel.py
│   │   │   │   ├── ncsnpp.py
│   │   │   │   ├── schroedinger_bridge.py
│   │   │   │   └── transformerunet.py
│   │   │   └── utils
│   │   │       ├── audio.py
│   │   │       ├── callbacks.py
│   │   │       ├── __init__.py
│   │   │       ├── maxine.py
│   │   │       └── transforms.py
│   │   └── README.md
│   ├── avlm
│   │   ├── data
│   │   │   ├── energon
│   │   │   │   ├── avlm_data_module.py
│   │   │   │   ├── avlm_sample_config.py
│   │   │   │   ├── avlm_task_encoder.py
│   │   │   │   ├── calculate_media_seq_length.py
│   │   │   │   └── __init__.py
│   │   │   ├── __init__.py
│   │   │   └── mock.py
│   │   ├── __init__.py
│   │   ├── model
│   │   │   ├── avlm.py
│   │   │   ├── base.py
│   │   │   └── __init__.py
│   │   └── recipes
│   │       ├── avlm_8b.py
│   │       └── __init__.py
│   ├── common
│   │   ├── callbacks
│   │   │   ├── callbacks.py
│   │   │   ├── ema.py
│   │   │   ├── __init__.py
│   │   │   └── ipl_epoch_stopper.py
│   │   ├── data
│   │   │   ├── blendable_dataset.py
│   │   │   ├── data_samplers.py
│   │   │   ├── dataset.py
│   │   │   ├── fallback.py
│   │   │   ├── helpers.cpp
│   │   │   ├── __init__.py
│   │   │   ├── lhotse
│   │   │   │   ├── cutset.py
│   │   │   │   ├── dataloader.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── nemo_adapters.py
│   │   │   │   ├── sampling.py
│   │   │   │   └── text_adapters.py
│   │   │   ├── Makefile
│   │   │   ├── prompt_fn.py
│   │   │   └── utils.py
│   │   ├── __init__.py
│   │   ├── losses
│   │   │   ├── aggregator.py
│   │   │   ├── bce_logits_loss.py
│   │   │   ├── cross_entropy.py
│   │   │   ├── __init__.py
│   │   │   ├── mse_loss.py
│   │   │   ├── multi_similarity_loss.py
│   │   │   ├── smoothed_cross_entropy.py
│   │   │   └── spanning_loss.py
│   │   ├── metrics
│   │   │   ├── classification_accuracy.py
│   │   │   ├── global_average_loss_metric.py
│   │   │   ├── __init__.py
│   │   │   ├── metric_string_to_torchmetric.py
│   │   │   ├── perf_metrics.py
│   │   │   ├── perplexity.py
│   │   │   └── punct_er.py
│   │   ├── modules
│   │   │   ├── adapters
│   │   │   │   ├── fused_bias_gelu.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── mcore_mixins.py
│   │   │   │   ├── parallel_adapters.py
│   │   │   │   └── qlora.py
│   │   │   ├── __init__.py
│   │   │   ├── megatron_init.py
│   │   │   └── megatron.py
│   │   ├── parts
│   │   │   ├── adapter_modules.py
│   │   │   ├── __init__.py
│   │   │   ├── megatron_trainer_builder.py
│   │   │   ├── mlm_scorer.py
│   │   │   ├── multi_layer_perceptron.py
│   │   │   ├── nemo_run_utils.py
│   │   │   ├── nlp_overrides.py
│   │   │   ├── optional_cuda_graphs.py
│   │   │   ├── patch_utils.py
│   │   │   ├── perf_metrics_utils.py
│   │   │   ├── preprocessing
│   │   │   │   ├── cleaners.py
│   │   │   │   ├── collections.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── manifest.py
│   │   │   │   └── parsers.py
│   │   │   ├── ptl_overrides.py
│   │   │   ├── rnn.py
│   │   │   ├── skills_utils.py
│   │   │   ├── transformer_utils.py
│   │   │   └── utils.py
│   │   ├── prompts
│   │   │   ├── canary2.py
│   │   │   ├── canary.py
│   │   │   ├── example.py
│   │   │   ├── formatter.py
│   │   │   ├── gemma.py
│   │   │   ├── __init__.py
│   │   │   ├── llama.py
│   │   │   ├── mistral.py
│   │   │   ├── nemotron_h.py
│   │   │   ├── phi2.py
│   │   │   ├── plain.py
│   │   │   ├── qwen.py
│   │   │   └── t5nmt.py
│   │   ├── tokenizers
│   │   │   ├── aggregate_tokenizer.py
│   │   │   ├── bytelevel_tokenizers.py
│   │   │   ├── canary_tokenizer.py
│   │   │   ├── char_tokenizer.py
│   │   │   ├── chat_template_mixin.py
│   │   │   ├── chinese_tokenizers.py
│   │   │   ├── column_coder.py
│   │   │   ├── en_ja_tokenizers.py
│   │   │   ├── fairseq_tokenizer.py
│   │   │   ├── huggingface
│   │   │   │   ├── auto_tokenizer.py
│   │   │   │   └── __init__.py
│   │   │   ├── indic_tokenizers.py
│   │   │   ├── __init__.py
│   │   │   ├── megatron_utils.py
│   │   │   ├── moses_tokenizers.py
│   │   │   ├── null_tokenizer.py
│   │   │   ├── regex_tokenizer.py
│   │   │   ├── sentencepiece_tokenizer.py
│   │   │   ├── tabular_tokenizer.py
│   │   │   ├── text_to_speech
│   │   │   │   ├── __init__.py
│   │   │   │   ├── ipa_lexicon.py
│   │   │   │   ├── tokenizer_utils.py
│   │   │   │   ├── tokenizer_wrapper.py
│   │   │   │   └── tts_tokenizers.py
│   │   │   ├── tiktoken_tokenizer.py
│   │   │   ├── tokenizer_spec.py
│   │   │   ├── tokenizer_utils.py
│   │   │   ├── word_tokenizer.py
│   │   │   └── youtokentome_tokenizer.py
│   │   └── video_tokenizers
│   │       ├── cosmos_tokenizer.py
│   │       ├── __init__.py
│   │       ├── modules
│   │       │   ├── distributions.py
│   │       │   ├── __init__.py
│   │       │   ├── layers2d.py
│   │       │   ├── layers3d.py
│   │       │   ├── patching.py
│   │       │   ├── quantizers.py
│   │       │   └── utils.py
│   │       ├── networks
│   │       │   ├── configs.py
│   │       │   ├── continuous_image.py
│   │       │   ├── continuous_video.py
│   │       │   ├── discrete_image.py
│   │       │   ├── discrete_video.py
│   │       │   └── __init__.py
│   │       ├── README.md
│   │       └── utils.py
│   ├── diffusion
│   │   ├── assets
│   │   │   ├── mixed_training.png
│   │   │   ├── pipeline_conditioning.png
│   │   │   └── st_dit_hybrid_parallel.png
│   │   ├── data
│   │   │   ├── diffusion_energon_datamodule.py
│   │   │   ├── diffusion_fake_datamodule.py
│   │   │   ├── diffusion_mock_datamodule.py
│   │   │   ├── diffusion_taskencoder.py
│   │   │   ├── __init__.py
│   │   │   ├── prepare_energon_dataset.py
│   │   │   └── readme.rst
│   │   ├── encoders
│   │   │   ├── conditioner.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── models
│   │   │   ├── dit
│   │   │   │   ├── dit_attention.py
│   │   │   │   ├── dit_embeddings.py
│   │   │   │   ├── dit_layer_spec.py
│   │   │   │   ├── dit_model.py
│   │   │   │   └── __init__.py
│   │   │   ├── dit_llama
│   │   │   │   ├── dit_llama_layer_spec.py
│   │   │   │   ├── dit_llama_model.py
│   │   │   │   └── __init__.py
│   │   │   ├── flux
│   │   │   │   ├── __init__.py
│   │   │   │   ├── layers.py
│   │   │   │   ├── model.py
│   │   │   │   └── pipeline.py
│   │   │   ├── flux_controlnet
│   │   │   │   ├── __init__.py
│   │   │   │   ├── layers.py
│   │   │   │   └── model.py
│   │   │   ├── __init__.py
│   │   │   └── model.py
│   │   ├── readme.rst
│   │   ├── recipes
│   │   │   ├── flux_12b.py
│   │   │   ├── flux_535m.py
│   │   │   └── __init__.py
│   │   ├── sampler
│   │   │   ├── batch_ops.py
│   │   │   ├── context_parallel.py
│   │   │   ├── edm
│   │   │   │   ├── edm_pipeline.py
│   │   │   │   ├── edm.py
│   │   │   │   └── __init__.py
│   │   │   ├── flow_matching
│   │   │   │   ├── flow_match_euler_discrete.py
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   ├── utils
│   │   │   ├── flux_ckpt_converter.py
│   │   │   ├── flux_pipeline_utils.py
│   │   │   ├── __init__.py
│   │   │   └── mcore_parallel_utils.py
│   │   └── vae
│   │       ├── autoencoder.py
│   │       ├── autovae.py
│   │       ├── blocks.py
│   │       ├── contperceptual_loss.py
│   │       ├── diffusers_vae.py
│   │       ├── __init__.py
│   │       ├── readme.rst
│   │       ├── test_autovae.py
│   │       ├── train_vae.py
│   │       ├── train_vae.sh
│   │       ├── vae16x
│   │       │   └── config.json
│   │       └── validate_vae.py
│   ├── __init__.py
│   ├── llm
│   │   ├── api.py
│   │   ├── bert
│   │   │   ├── data
│   │   │   │   ├── core.py
│   │   │   │   ├── fine_tuning.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── mock.py
│   │   │   │   ├── pre_training.py
│   │   │   │   └── specter.py
│   │   │   ├── __init__.py
│   │   │   ├── loss.py
│   │   │   └── model
│   │   │       ├── base.py
│   │   │       ├── bert.py
│   │   │       ├── bert_spec.py
│   │   │       ├── embedding.py
│   │   │       └── __init__.py
│   │   ├── fn
│   │   │   ├── activation.py
│   │   │   ├── base.py
│   │   │   ├── __init__.py
│   │   │   └── mixin.py
│   │   ├── gpt
│   │   │   ├── data
│   │   │   │   ├── alpaca.py
│   │   │   │   ├── api.py
│   │   │   │   ├── chat.py
│   │   │   │   ├── core.py
│   │   │   │   ├── dolly.py
│   │   │   │   ├── fine_tuning.py
│   │   │   │   ├── hf_dataset_packed_sequence.py
│   │   │   │   ├── hf_dataset.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── megatron
│   │   │   │   │   ├── hyena
│   │   │   │   │   │   ├── config.py
│   │   │   │   │   │   ├── evo2_dataset.py
│   │   │   │   │   │   └── __init__.py
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── mlperf_govreport.py
│   │   │   │   ├── mock.py
│   │   │   │   ├── packed_sequence.py
│   │   │   │   ├── pre_training.py
│   │   │   │   ├── reranker.py
│   │   │   │   ├── retrieval.py
│   │   │   │   ├── squad.py
│   │   │   │   └── utils.py
│   │   │   ├── __init__.py
│   │   │   └── model
│   │   │       ├── baichuan.py
│   │   │       ├── base.py
│   │   │       ├── chatglm.py
│   │   │       ├── deepseek.py
│   │   │       ├── gemma2.py
│   │   │       ├── gemma3.py
│   │   │       ├── gemma.py
│   │   │       ├── gpt_oss.py
│   │   │       ├── hf_llama_embedding.py
│   │   │       ├── hyena.py
│   │   │       ├── __init__.py
│   │   │       ├── llama4_utils.py
│   │   │       ├── llama_embedding.py
│   │   │       ├── llama_nemotron_config.py
│   │   │       ├── llama_nemotron.py
│   │   │       ├── llama.py
│   │   │       ├── megatron
│   │   │       │   ├── hyena
│   │   │       │   │   ├── engine.py
│   │   │       │   │   ├── hyena_block.py
│   │   │       │   │   ├── hyena_config.py
│   │   │       │   │   ├── hyena_hybrid_layer_allocation.py
│   │   │       │   │   ├── hyena_layer.py
│   │   │       │   │   ├── hyena_layer_specs.py
│   │   │       │   │   ├── hyena_mixer.py
│   │   │       │   │   ├── hyena_model.py
│   │   │       │   │   ├── hyena_utils.py
│   │   │       │   │   ├── __init__.py
│   │   │       │   │   └── te_compat.py
│   │   │       │   └── __init__.py
│   │   │       ├── mistral.py
│   │   │       ├── mixtral.py
│   │   │       ├── nemotron.py
│   │   │       ├── phi3mini.py
│   │   │       ├── qwen2.py
│   │   │       ├── qwen3.py
│   │   │       ├── reranker.py
│   │   │       ├── ssm.py
│   │   │       ├── starcoder2.py
│   │   │       └── starcoder.py
│   │   ├── inference
│   │   │   ├── base.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── modelopt
│   │   │   ├── distill
│   │   │   │   ├── __init__.py
│   │   │   │   ├── loss.py
│   │   │   │   ├── model.py
│   │   │   │   └── utils.py
│   │   │   ├── __init__.py
│   │   │   ├── model_utils.py
│   │   │   ├── prune
│   │   │   │   ├── __init__.py
│   │   │   │   └── pruner.py
│   │   │   ├── quantization
│   │   │   │   ├── __init__.py
│   │   │   │   ├── quant_cfg_choices.py
│   │   │   │   ├── quantizer.py
│   │   │   │   └── utils.py
│   │   │   ├── recipes
│   │   │   │   ├── distillation_recipe.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── prune_recipe.py
│   │   │   └── speculative
│   │   │       ├── __init__.py
│   │   │       └── model_transform.py
│   │   ├── peft
│   │   │   ├── api.py
│   │   │   ├── canonical_lora.py
│   │   │   ├── dora.py
│   │   │   ├── __init__.py
│   │   │   ├── lora.py
│   │   │   ├── module_matcher.py
│   │   │   └── utils.py
│   │   ├── README.md
│   │   ├── recipes
│   │   │   ├── ADD-RECIPE.md
│   │   │   ├── baichuan2_7b.py
│   │   │   ├── bert_110m.py
│   │   │   ├── bert_340m.py
│   │   │   ├── bert_embedding.py
│   │   │   ├── bert.py
│   │   │   ├── callbacks
│   │   │   │   ├── common.py
│   │   │   │   └── __init__.py
│   │   │   ├── chatglm3_6b.py
│   │   │   ├── CONFIGURATION-HIERARCHY.md
│   │   │   ├── deepseek.py
│   │   │   ├── deepseek_v2_lite.py
│   │   │   ├── deepseek_v2.py
│   │   │   ├── deepseek_v3.py
│   │   │   ├── e5_340m.py
│   │   │   ├── finetune_default.py
│   │   │   ├── gemma2_27b.py
│   │   │   ├── gemma2_2b.py
│   │   │   ├── gemma2_9b.py
│   │   │   ├── gemma_2b.py
│   │   │   ├── gemma2.py
│   │   │   ├── gemma3_1b.py
│   │   │   ├── gemma_7b.py
│   │   │   ├── gpt3_175b.py
│   │   │   ├── gpt_oss_120b.py
│   │   │   ├── gpt_oss_20b.py
│   │   │   ├── hyena_1b.py
│   │   │   ├── hyena_40b.py
│   │   │   ├── hyena_7b.py
│   │   │   ├── hyena_base.py
│   │   │   ├── __init__.py
│   │   │   ├── llama2_7b.py
│   │   │   ├── llama31_405b.py
│   │   │   ├── llama31_70b.py
│   │   │   ├── llama31_8b.py
│   │   │   ├── llama31_nemotron_70b.py
│   │   │   ├── llama31_nemotron_nano_8b.py
│   │   │   ├── llama31_nemotron_ultra_253b.py
│   │   │   ├── llama32_1b.py
│   │   │   ├── llama32_3b.py
│   │   │   ├── llama33_nemotron_super_49b.py
│   │   │   ├── llama3_70b_16k.py
│   │   │   ├── llama3_70b_64k.py
│   │   │   ├── llama3_70b.py
│   │   │   ├── llama3_8b_128k.py
│   │   │   ├── llama3_8b_16k.py
│   │   │   ├── llama3_8b_64k.py
│   │   │   ├── llama3_8b.py
│   │   │   ├── llama4_e128.py
│   │   │   ├── llama4_e16.py
│   │   │   ├── llama_embedding_1b.py
│   │   │   ├── llama_embedding_3b.py
│   │   │   ├── llama_reranker_1b.py
│   │   │   ├── log
│   │   │   │   ├── default.py
│   │   │   │   └── __init__.py
│   │   │   ├── mamba2_130m.py
│   │   │   ├── mamba2_1_3b.py
│   │   │   ├── mamba2_2_7b.py
│   │   │   ├── mamba2_370m.py
│   │   │   ├── mamba2_780m.py
│   │   │   ├── mamba2_8b.py
│   │   │   ├── mamba2_hybrid_8b.py
│   │   │   ├── mistral_7b.py
│   │   │   ├── mistral_nemo_12b.py
│   │   │   ├── mistral_small3_24b.py
│   │   │   ├── mixtral_8x22b_64k.py
│   │   │   ├── mixtral_8x22b.py
│   │   │   ├── mixtral_8x7b_16k.py
│   │   │   ├── mixtral_8x7b_64k.py
│   │   │   ├── mixtral_8x7b.py
│   │   │   ├── nemotron3_22b_16k.py
│   │   │   ├── nemotron3_22b_64k.py
│   │   │   ├── nemotron3_22b.py
│   │   │   ├── nemotron3_4b.py
│   │   │   ├── nemotron3_8b.py
│   │   │   ├── nemotron4_15b_16k.py
│   │   │   ├── nemotron4_15b_64k.py
│   │   │   ├── nemotron4_15b.py
│   │   │   ├── nemotron4_340b.py
│   │   │   ├── nemotronh_47b.py
│   │   │   ├── nemotronh_4b.py
│   │   │   ├── nemotronh_56b.py
│   │   │   ├── nemotronh_8b.py
│   │   │   ├── nemotron_nano_12b_v2.py
│   │   │   ├── nemotron_nano_9b_v2.py
│   │   │   ├── nemotron.py
│   │   │   ├── optim
│   │   │   │   ├── adam.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── sgd.py
│   │   │   ├── phi3_mini_4k_instruct.py
│   │   │   ├── precision
│   │   │   │   ├── __init__.py
│   │   │   │   └── mixed_precision.py
│   │   │   ├── qwen2_1p5b.py
│   │   │   ├── qwen2_500m.py
│   │   │   ├── qwen25_14b.py
│   │   │   ├── qwen25_1p5b.py
│   │   │   ├── qwen25_32b.py
│   │   │   ├── qwen25_500m.py
│   │   │   ├── qwen25_72b.py
│   │   │   ├── qwen25_7b.py
│   │   │   ├── qwen2_72b.py
│   │   │   ├── qwen2_7b.py
│   │   │   ├── qwen2.py
│   │   │   ├── qwen3_14b.py
│   │   │   ├── qwen3_1p7b.py
│   │   │   ├── qwen3_235b_a22b.py
│   │   │   ├── qwen3_30b_a3b.py
│   │   │   ├── qwen3_32b.py
│   │   │   ├── qwen3_4b.py
│   │   │   ├── qwen3_600m.py
│   │   │   ├── qwen3_8b.py
│   │   │   ├── qwen3.py
│   │   │   ├── README.md
│   │   │   ├── run
│   │   │   │   ├── executor.py
│   │   │   │   └── __init__.py
│   │   │   ├── starcoder_15b.py
│   │   │   ├── starcoder2_15b.py
│   │   │   ├── starcoder2_3b.py
│   │   │   ├── starcoder2_7b.py
│   │   │   ├── starcoder2.py
│   │   │   ├── t5_11b.py
│   │   │   ├── t5_220m.py
│   │   │   ├── t5_3b.py
│   │   │   └── tp_overlap_configs
│   │   │       ├── __init__.py
│   │   │       └── userbuffers.py
│   │   ├── t5
│   │   │   ├── data
│   │   │   │   ├── core.py
│   │   │   │   ├── fine_tuning.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── mock.py
│   │   │   │   ├── pre_training.py
│   │   │   │   └── squad.py
│   │   │   ├── __init__.py
│   │   │   └── model
│   │   │       ├── __init__.py
│   │   │       └── t5.py
│   │   ├── tools
│   │   │   ├── auto_configurator
│   │   │   │   ├── core
│   │   │   │   │   ├── base_config.py
│   │   │   │   │   ├── calculate_performance.py
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── training_config.py
│   │   │   │   │   └── utils.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── runner.py
│   │   │   └── __init__.py
│   │   └── utils.py
│   ├── multimodal
│   │   ├── data
│   │   │   ├── clip
│   │   │   │   ├── augmentations
│   │   │   │   │   ├── augmentations.py
│   │   │   │   │   └── __init__.py
│   │   │   │   ├── clip_dataset.py
│   │   │   │   ├── imagenet_zeroshot_data.py
│   │   │   │   └── __init__.py
│   │   │   ├── common
│   │   │   │   ├── data_samplers.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── utils.py
│   │   │   │   ├── webdataset.py
│   │   │   │   └── webdataset_s3.py
│   │   │   ├── energon
│   │   │   │   ├── base.py
│   │   │   │   ├── config.py
│   │   │   │   ├── conversation.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── sample_encoder.py
│   │   │   │   └── task_encoder.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── README.md
│   │   ├── speech_cv
│   │   │   ├── data
│   │   │   │   ├── __init__.py
│   │   │   │   ├── video_to_text_dataset.py
│   │   │   │   └── video_to_text.py
│   │   │   ├── __init__.py
│   │   │   ├── models
│   │   │   │   ├── __init__.py
│   │   │   │   ├── visual_ctc_bpe_models.py
│   │   │   │   ├── visual_ctc_models.py
│   │   │   │   ├── visual_hybrid_rnnt_ctc_bpe_models.py
│   │   │   │   ├── visual_hybrid_rnnt_ctc_models.py
│   │   │   │   ├── visual_rnnt_bpe_models.py
│   │   │   │   └── visual_rnnt_models.py
│   │   │   ├── modules
│   │   │   │   ├── __init__.py
│   │   │   │   ├── linear_projection_video_front_end.py
│   │   │   │   ├── resnet_video_front_end.py
│   │   │   │   ├── video_augment.py
│   │   │   │   └── video_preprocessing.py
│   │   │   └── parts
│   │   │       ├── __init__.py
│   │   │       ├── preprocessing
│   │   │       │   ├── features.py
│   │   │       │   └── __init__.py
│   │   │       └── submodules
│   │   │           ├── conv2d.py
│   │   │           ├── global_avg_pool2d.py
│   │   │           ├── __init__.py
│   │   │           ├── permute.py
│   │   │           ├── resnet_block.py
│   │   │           ├── resnet_bottleneck_block.py
│   │   │           └── resnet.py
│   │   └── speech_llm
│   │       ├── data
│   │       │   ├── audio_text_dataset.py
│   │       │   ├── build_dataset.py
│   │       │   ├── __init__.py
│   │       │   └── lhotse_dataset.py
│   │       ├── __init__.py
│   │       ├── models
│   │       │   ├── __init__.py
│   │       │   ├── modular_models.py
│   │       │   └── modular_t5_models.py
│   │       ├── modules
│   │       │   ├── common
│   │       │   │   ├── audio_text_generation_strategy.py
│   │       │   │   ├── audio_text_generation_utils.py
│   │       │   │   ├── __init__.py
│   │       │   │   ├── text_generation_strategy.py
│   │       │   │   └── text_generation_utils.py
│   │       │   ├── __init__.py
│   │       │   ├── modality_adapters.py
│   │       │   ├── perception_modules.py
│   │       │   └── transformer_decoders.py
│   │       └── parts
│   │           ├── __init__.py
│   │           ├── mixins
│   │           │   ├── adapter_mixin.py
│   │           │   └── __init__.py
│   │           ├── peft_config.py
│   │           └── utils
│   │               ├── data_utils.py
│   │               └── __init__.py
│   ├── multimodal_autoregressive
│   │   ├── data
│   │   │   ├── __init__.py
│   │   │   ├── preprocess_coyo_emu3_tokenizer.py
│   │   │   ├── preprocess_pokemon_blip_cosmos_tokenizer.py
│   │   │   └── README.md
│   │   ├── __init__.py
│   │   └── tokenizer
│   │       ├── cosmos_multimodal_tokenizer.py
│   │       ├── cosmos_vision_tokens.txt
│   │       ├── emu3.tiktoken
│   │       ├── __init__.py
│   │       ├── special_tokens_map.json
│   │       └── tokenizer_config.json
│   ├── speechlm
│   │   ├── api.py
│   │   ├── data
│   │   │   ├── audio_to_text_module.py
│   │   │   ├── data_sampler.py
│   │   │   ├── dataset
│   │   │   │   ├── audio_text_dataset.py
│   │   │   │   ├── audio_text_lhotse_dataset.py
│   │   │   │   ├── data_utils.py
│   │   │   │   └── __init__.py
│   │   │   ├── __init__.py
│   │   │   └── text_processing.py
│   │   ├── __init__.py
│   │   ├── models
│   │   │   ├── base.py
│   │   │   ├── __init__.py
│   │   │   └── speech_to_text_llm_model.py
│   │   ├── modules
│   │   │   ├── asr_module.py
│   │   │   ├── __init__.py
│   │   │   └── modality_adapter.py
│   │   ├── recipes
│   │   │   ├── __init__.py
│   │   │   ├── optim
│   │   │   │   ├── adam.py
│   │   │   │   └── __init__.py
│   │   │   └── pipeline.py
│   │   ├── strategies
│   │   │   ├── __init__.py
│   │   │   └── megatron_strategy.py
│   │   └── utils
│   │       ├── hydra_utils.py
│   │       ├── __init__.py
│   │       ├── io.py
│   │       ├── model_transform.py
│   │       ├── resume.py
│   │       └── text_generation
│   │           ├── audio_text_generation_strategy.py
│   │           ├── audio_text_generation_utils.py
│   │           └── __init__.py
│   ├── speechlm2
│   │   ├── data
│   │   │   ├── datamodule.py
│   │   │   ├── duplex_ear_tts_dataset.py
│   │   │   ├── __init__.py
│   │   │   ├── s2s_dataset.py
│   │   │   ├── salm_dataset.py
│   │   │   └── utils.py
│   │   ├── __init__.py
│   │   ├── models
│   │   │   ├── duplex_ear_tts.py
│   │   │   ├── duplex_s2s_model.py
│   │   │   ├── duplex_s2s_speech_decoder_model.py
│   │   │   ├── __init__.py
│   │   │   └── salm.py
│   │   ├── modules
│   │   │   ├── ear_tts_model.py
│   │   │   ├── ear_tts_vae_codec.py
│   │   │   ├── __init__.py
│   │   │   ├── perception.py
│   │   │   └── speech_generation.py
│   │   └── parts
│   │       ├── hf_hub.py
│   │       ├── __init__.py
│   │       ├── lora.py
│   │       ├── metrics
│   │       │   ├── asr_bleu.py
│   │       │   ├── asr_cer_wer.py
│   │       │   ├── bleu.py
│   │       │   ├── __init__.py
│   │       │   ├── results_logger.py
│   │       │   ├── secs.py
│   │       │   ├── token_accuracy.py
│   │       │   └── wer.py
│   │       ├── nsight.py
│   │       ├── optim_setup.py
│   │       ├── precision.py
│   │       └── pretrained.py
│   ├── tts
│   │   ├── data
│   │   │   ├── dataset.py
│   │   │   ├── __init__.py
│   │   │   ├── text_to_speech_dataset_lhotse.py
│   │   │   ├── text_to_speech_dataset.py
│   │   │   └── vocoder_dataset.py
│   │   ├── g2p
│   │   │   ├── data
│   │   │   │   ├── ctc.py
│   │   │   │   ├── heteronym_classification.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── t5.py
│   │   │   ├── __init__.py
│   │   │   ├── models
│   │   │   │   ├── base.py
│   │   │   │   ├── ctc.py
│   │   │   │   ├── en_us_arpabet.py
│   │   │   │   ├── i18n_ipa.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── ja_jp_ipa.py
│   │   │   │   ├── t5.py
│   │   │   │   ├── token_classifier.py
│   │   │   │   └── zh_cn_pinyin.py
│   │   │   ├── modules.py
│   │   │   └── utils.py
│   │   ├── __init__.py
│   │   ├── losses
│   │   │   ├── aligner_loss.py
│   │   │   ├── audio_codec_loss.py
│   │   │   ├── fastpitchloss.py
│   │   │   ├── hifigan_losses.py
│   │   │   ├── __init__.py
│   │   │   ├── radttsloss.py
│   │   │   ├── spectrogram_enhancer_losses.py
│   │   │   ├── stftlosses.py
│   │   │   ├── tacotron2loss.py
│   │   │   ├── vits_losses.py
│   │   │   └── waveglowloss.py
│   │   ├── metrics
│   │   │   ├── classification_report.py
│   │   │   ├── frechet_codec_distance.py
│   │   │   ├── __init__.py
│   │   │   └── score_metrics.py
│   │   ├── models
│   │   │   ├── aligner.py
│   │   │   ├── audio_codec.py
│   │   │   ├── base.py
│   │   │   ├── fastpitch.py
│   │   │   ├── fastpitch_ssl.py
│   │   │   ├── hifigan.py
│   │   │   ├── __init__.py
│   │   │   ├── magpietts_preference_optimization.py
│   │   │   ├── magpietts.py
│   │   │   ├── mixer_tts.py
│   │   │   ├── radtts.py
│   │   │   ├── spectrogram_enhancer.py
│   │   │   ├── ssl_tts.py
│   │   │   ├── tacotron2.py
│   │   │   ├── two_stages.py
│   │   │   ├── univnet.py
│   │   │   ├── vits.py
│   │   │   └── waveglow.py
│   │   ├── modules
│   │   │   ├── adapters.py
│   │   │   ├── aligner.py
│   │   │   ├── attribute_prediction_model.py
│   │   │   ├── audio_codec_modules.py
│   │   │   ├── common.py
│   │   │   ├── encodec_modules.py
│   │   │   ├── fastpitch.py
│   │   │   ├── hifigan_modules.py
│   │   │   ├── __init__.py
│   │   │   ├── magpietts_inference
│   │   │   │   ├── evaluate_generated_audio.py
│   │   │   │   ├── evaluation.py
│   │   │   │   ├── inference.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── utils.py
│   │   │   │   └── visualization.py
│   │   │   ├── magpietts_modules.py
│   │   │   ├── mixer_tts.py
│   │   │   ├── monotonic_align
│   │   │   │   ├── __init__.py
│   │   │   │   └── numba_core.py
│   │   │   ├── radtts.py
│   │   │   ├── spectrogram_enhancer.py
│   │   │   ├── ssl_tts.py
│   │   │   ├── submodules.py
│   │   │   ├── tacotron2.py
│   │   │   ├── transformer_2501.py
│   │   │   ├── transformer.py
│   │   │   ├── univnet_modules.py
│   │   │   ├── utmosv2.py
│   │   │   ├── vits_modules.py
│   │   │   └── waveglow.py
│   │   ├── parts
│   │   │   ├── __init__.py
│   │   │   ├── mixins
│   │   │   │   ├── fastpitch_adapter_mixins.py
│   │   │   │   └── __init__.py
│   │   │   ├── preprocessing
│   │   │   │   ├── audio_trimming.py
│   │   │   │   ├── feature_processors.py
│   │   │   │   ├── features.py
│   │   │   │   └── __init__.py
│   │   │   └── utils
│   │   │       ├── callbacks.py
│   │   │       ├── distributed.py
│   │   │       ├── helpers.py
│   │   │       ├── __init__.py
│   │   │       ├── splines.py
│   │   │       └── tts_dataset_utils.py
│   │   ├── README.md
│   │   └── torch
│   │       ├── g2ps.py
│   │       ├── __init__.py
│   │       ├── tts_data_types.py
│   │       └── tts_tokenizers.py
│   ├── vision
│   │   ├── data
│   │   │   ├── imagenet_classnames.py
│   │   │   ├── __init__.py
│   │   │   └── megatron
│   │   │       ├── autoaugment.py
│   │   │       ├── data_samplers.py
│   │   │       ├── image_folder.py
│   │   │       ├── __init__.py
│   │   │       └── vit_dataset.py
│   │   └── __init__.py
│   └── vlm
│       ├── api.py
│       ├── clip
│       │   ├── data
│       │   │   ├── clip_data_module.py
│       │   │   ├── __init__.py
│       │   │   └── mock.py
│       │   ├── __init__.py
│       │   ├── loss
│       │   │   ├── clip_loss.py
│       │   │   └── __init__.py
│       │   └── model
│       │       ├── base.py
│       │       ├── clip.py
│       │       └── __init__.py
│       ├── data
│       │   ├── data_module.py
│       │   ├── __init__.py
│       │   ├── task_encoder.py
│       │   └── utils.py
│       ├── gemma3vl
│       │   ├── data
│       │   │   ├── __init__.py
│       │   │   ├── mock.py
│       │   │   └── task_encoder.py
│       │   ├── __init__.py
│       │   └── model
│       │       ├── base.py
│       │       ├── gemma3vl.py
│       │       ├── __init__.py
│       │       └── vision.py
│       ├── hf
│       │   ├── data
│       │   │   ├── hf_dataset.py
│       │   │   └── __init__.py
│       │   ├── __init__.py
│       │   └── model
│       │       └── __init__.py
│       ├── inference
│       │   ├── base.py
│       │   ├── __init__.py
│       │   ├── llava_inference_wrapper.py
│       │   ├── mllama_inference_wrapper.py
│       │   ├── qwenvl_inference_wrapper.py
│       │   ├── vlm_engine.py
│       │   └── vlm_inference_controller.py
│       ├── __init__.py
│       ├── layer_specs.py
│       ├── llama4
│       │   ├── data
│       │   │   ├── __init__.py
│       │   │   ├── mock.py
│       │   │   └── task_encoder.py
│       │   ├── __init__.py
│       │   └── model
│       │       ├── base.py
│       │       ├── __init__.py
│       │       ├── llama4_omni.py
│       │       └── vision.py
│       ├── llava_next
│       │   ├── data
│       │   │   ├── __init__.py
│       │   │   ├── interleaved_sample_encoder.py
│       │   │   ├── mock.py
│       │   │   ├── sample.py
│       │   │   ├── task_encoder.py
│       │   │   ├── utils.py
│       │   │   └── vqa_sample_encoder.py
│       │   ├── __init__.py
│       │   └── model
│       │       ├── base.py
│       │       ├── __init__.py
│       │       ├── llava_next.py
│       │       └── utils.py
│       ├── mllama
│       │   ├── data
│       │   │   ├── __init__.py
│       │   │   ├── mock.py
│       │   │   ├── preloaded.py
│       │   │   ├── sample_encoder.py
│       │   │   └── task_encoder.py
│       │   ├── __init__.py
│       │   └── model
│       │       ├── base.py
│       │       ├── __init__.py
│       │       ├── language.py
│       │       ├── mllama.py
│       │       ├── utils.py
│       │       └── vision.py
│       ├── modelopt
│       │   ├── __init__.py
│       │   └── model_utils.py
│       ├── neva
│       │   ├── data
│       │   │   ├── config.py
│       │   │   ├── conversation.py
│       │   │   ├── __init__.py
│       │   │   ├── mock.py
│       │   │   ├── multimodal_tokens.py
│       │   │   ├── preloaded.py
│       │   │   └── sequence_packing.py
│       │   ├── __init__.py
│       │   └── model
│       │       ├── base.py
│       │       ├── __init__.py
│       │       └── llava.py
│       ├── peft
│       │   ├── __init__.py
│       │   └── lora.py
│       ├── qwen2vl
│       │   ├── data
│       │   │   ├── config.py
│       │   │   ├── conversation.py
│       │   │   ├── __init__.py
│       │   │   ├── mock.py
│       │   │   ├── multimodal_tokens.py
│       │   │   ├── preloaded.py
│       │   │   └── task_encoder.py
│       │   ├── __init__.py
│       │   └── model
│       │       ├── api.py
│       │       ├── base.py
│       │       ├── __init__.py
│       │       ├── qwen2vl.py
│       │       └── vision.py
│       ├── recipes
│       │   ├── clip_b32.py
│       │   ├── gemma3vl_12b.py
│       │   ├── gemma3vl_27b.py
│       │   ├── gemma3vl_4b.py
│       │   ├── __init__.py
│       │   ├── llama4_omni_e128.py
│       │   ├── llama4_omni_e16.py
│       │   ├── llava15_13b.py
│       │   ├── llava15_7b.py
│       │   ├── llava_next_7b.py
│       │   ├── mllama_11b.py
│       │   ├── mllama_90b.py
│       │   ├── neva_llama3_8b.py
│       │   ├── qwen25vl_32b.py
│       │   ├── qwen25vl_7b.py
│       │   └── qwen2vl_2b.py
│       └── vision
│           ├── base.py
│           ├── clip_vit.py
│           ├── __init__.py
│           ├── intern_vit.py
│           └── siglip_vit.py
├── constants.py
├── core
│   ├── classes
│   │   ├── common.py
│   │   ├── dataset.py
│   │   ├── exportable.py
│   │   ├── __init__.py
│   │   ├── loss.py
│   │   ├── mixins
│   │   │   ├── access_mixins.py
│   │   │   ├── adapter_mixins.py
│   │   │   ├── adapter_mixin_strategies.py
│   │   │   ├── hf_io_mixin.py
│   │   │   └── __init__.py
│   │   ├── modelPT.py
│   │   └── module.py
│   ├── config
│   │   ├── base_config.py
│   │   ├── hydra_runner.py
│   │   ├── __init__.py
│   │   ├── modelPT.py
│   │   ├── optimizers.py
│   │   ├── pytorch_lightning.py
│   │   ├── pytorch.py
│   │   ├── schedulers.py
│   │   └── templates
│   │       ├── __init__.py
│   │       └── model_card.py
│   ├── connectors
│   │   ├── __init__.py
│   │   └── save_restore_connector.py
│   ├── __init__.py
│   ├── neural_types
│   │   ├── axes.py
│   │   ├── comparison.py
│   │   ├── elements.py
│   │   ├── __init__.py
│   │   └── neural_type.py
│   ├── optim
│   │   ├── adafactor.py
│   │   ├── adan.py
│   │   ├── distributed_adam.py
│   │   ├── __init__.py
│   │   ├── lr_scheduler.py
│   │   ├── mcore_optim.py
│   │   ├── megatron_fused_adam.py
│   │   ├── novograd.py
│   │   ├── optimizers.py
│   │   ├── optimizer_with_main_params.py
│   │   └── radam.py
│   └── utils
│       ├── cuda_python_utils.py
│       ├── __init__.py
│       ├── k2_guard.py
│       ├── k2_utils.py
│       ├── neural_type_utils.py
│       ├── numba_utils.py
│       ├── optional_libs.py
│       └── process_launcher
│           ├── __init__.py
│           └── launcher.py
├── export
│   ├── __init__.py
│   ├── multimodal
│   │   ├── build.py
│   │   ├── converter.py
│   │   ├── __init__.py
│   │   └── run.py
│   ├── onnx_llm_exporter.py
│   ├── quantize
│   │   ├── __init__.py
│   │   └── quantizer.py
│   ├── sentencepiece_tokenizer.py
│   ├── tarutils.py
│   ├── tensorrt_lazy_compiler.py
│   ├── tensorrt_llm.py
│   ├── tensorrt_mm_exporter.py
│   ├── tiktoken_tokenizer.py
│   ├── trt_llm
│   │   ├── converter
│   │   │   ├── __init__.py
│   │   │   ├── model_converter.py
│   │   │   ├── model_to_trt_llm_ckpt.py
│   │   │   └── utils.py
│   │   ├── __init__.py
│   │   ├── nemo_ckpt_loader
│   │   │   ├── __init__.py
│   │   │   └── nemo_file.py
│   │   ├── qnemo
│   │   │   ├── __init__.py
│   │   │   ├── qnemo_to_tensorrt_llm.py
│   │   │   ├── tokenizer_utils.py
│   │   │   └── utils.py
│   │   ├── tensorrt_llm_build.py
│   │   ├── tensorrt_llm_run.py
│   │   └── utils.py
│   ├── utils
│   │   ├── constants.py
│   │   ├── __init__.py
│   │   ├── lora_converter.py
│   │   ├── _mock_import.py
│   │   ├── model_loader.py
│   │   └── utils.py
│   ├── vllm
│   │   ├── __init__.py
│   │   ├── model_config.py
│   │   ├── model_converters.py
│   │   └── model_loader.py
│   ├── vllm_exporter.py
│   └── vllm_hf_exporter.py
├── __init__.py
├── lightning
│   ├── base_callback.py
│   ├── base.py
│   ├── callback_group.py
│   ├── ckpt_utils.py
│   ├── data.py
│   ├── fabric
│   │   ├── conversion.py
│   │   ├── fabric.py
│   │   ├── __init__.py
│   │   ├── plugins.py
│   │   └── strategies.py
│   ├── __init__.py
│   ├── io
│   │   ├── api.py
│   │   ├── artifact
│   │   │   ├── base.py
│   │   │   ├── file.py
│   │   │   ├── hf_auto.py
│   │   │   ├── __init__.py
│   │   │   └── pickle.py
│   │   ├── capture.py
│   │   ├── connector.py
│   │   ├── fdl_torch.py
│   │   ├── hf.py
│   │   ├── __init__.py
│   │   ├── mixin.py
│   │   ├── pl.py
│   │   ├── registry.py
│   │   ├── state.py
│   │   └── to_config.py
│   ├── megatron_init.py
│   ├── megatron_parallel.py
│   ├── nemo_logger.py
│   ├── one_logger_callback.py
│   ├── pytorch
│   │   ├── accelerate
│   │   │   ├── __init__.py
│   │   │   └── transformer_engine.py
│   │   ├── callbacks
│   │   │   ├── ddp_parity_checker.py
│   │   │   ├── debugging.py
│   │   │   ├── deepep.py
│   │   │   ├── flops_callback.py
│   │   │   ├── garbage_collection.py
│   │   │   ├── __init__.py
│   │   │   ├── jit_transform.py
│   │   │   ├── layer_freezer.py
│   │   │   ├── megatron_comm_overlap.py
│   │   │   ├── megatron_enable_experimental_callback.py
│   │   │   ├── memory_callback.py
│   │   │   ├── memory_profiler.py
│   │   │   ├── model_callback.py
│   │   │   ├── model_checkpoint.py
│   │   │   ├── model_transform.py
│   │   │   ├── moe_token_drop.py
│   │   │   ├── nsys.py
│   │   │   ├── optimizer_monitor.py
│   │   │   ├── peft.py
│   │   │   ├── preemption.py
│   │   │   ├── progress_bar.py
│   │   │   ├── progress_printer.py
│   │   │   ├── pytorch_profiler.py
│   │   │   ├── runtime_estimator.py
│   │   │   └── speed_monitor.py
│   │   ├── __init__.py
│   │   ├── local_ckpt.py
│   │   ├── optim
│   │   │   ├── base.py
│   │   │   ├── __init__.py
│   │   │   ├── lr_scheduler.py
│   │   │   ├── megatron.py
│   │   │   └── pytorch.py
│   │   ├── plugins
│   │   │   ├── data_sampler.py
│   │   │   ├── __init__.py
│   │   │   └── mixed_precision.py
│   │   ├── strategies
│   │   │   ├── fsdp2_strategy.py
│   │   │   ├── fsdp_strategy.py
│   │   │   ├── __init__.py
│   │   │   ├── megatron_strategy.py
│   │   │   └── utils.py
│   │   ├── trainer.py
│   │   └── utils.py
│   ├── README.md
│   ├── resume.py
│   ├── run
│   │   ├── __init__.py
│   │   └── plugins.py
│   └── _strategy_lib.py
├── package_info.py
├── README.md
├── RESULTADOS
│   ├── jerarquia.py
│   └── tree_output.txt
└── utils
    ├── app_state.py
    ├── arguments.py
    ├── callbacks
    │   ├── checkpointing_context.py
    │   ├── cuda_graph.py
    │   ├── dist_ckpt_io.py
    │   ├── __init__.py
    │   ├── nemo_model_checkpoint.py
    │   ├── preemption.py
    │   └── s3_checkpoint_io.py
    ├── cast_utils.py
    ├── cloud.py
    ├── config_utils.py
    ├── data_utils.py
    ├── debug_hook.py
    ├── decorators
    │   ├── deprecated.py
    │   ├── experimental.py
    │   ├── __init__.py
    │   └── port_docs.py
    ├── distributed.py
    ├── dtype.py
    ├── enum.py
    ├── env_var_parsing.py
    ├── exceptions.py
    ├── exp_manager.py
    ├── export_utils.py
    ├── file_utils.py
    ├── flops_formulas.py
    ├── formatters
    │   ├── base.py
    │   ├── colors.py
    │   ├── __init__.py
    │   └── utils.py
    ├── get_rank.py
    ├── hyena_flops_formulas.py
    ├── import_utils.py
    ├── __init__.py
    ├── lightning_logger_patch.py
    ├── loggers
    │   ├── clearml_logger.py
    │   ├── dllogger.py
    │   ├── __init__.py
    │   └── mlflow_logger.py
    ├── mcore_logger.py
    ├── megatron_utils.py
    ├── metaclasses.py
    ├── model_utils.py
    ├── msc_utils.py
    ├── nemo_logging.py
    ├── notebook_utils.py
    ├── nvtx.py
    ├── s3_dirpath_utils.py
    ├── s3_utils.py
    ├── sequence_packing_utils.py
    ├── te_utils.py
    ├── timers.py
    ├── trainer_utils.py
    └── trt_utils.py