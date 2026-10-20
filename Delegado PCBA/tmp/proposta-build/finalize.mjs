import path from 'node:path';
import {pathToFileURL} from 'node:url';
process.env.RUNTIME_NODE_MODULES='C:/Users/Atr3mis/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const workspaceDir='C:/Users/Atr3mis/OneDrive/Documentos/Concursos/Delegado PCBA';
const skill='C:/Users/Atr3mis/.codex/plugins/cache/openai-primary-runtime/presentations/26.1011.11113/skills/presentations';
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
console.log(await finalizePresentation({workspaceDir,
 candidatePath:path.join(workspaceDir,'tmp/proposta-build/candidate.pptx'),
 finalPath:path.join(workspaceDir,'output/Proposta de Honorarios Advocaticios.pptx'),
 pythonExecutable:'C:/Users/Atr3mis/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit'],
 fontPolicy:{basis:'design',families:['Arial']},verifyArtifactToolImport:true,
 receiptPath:path.join(workspaceDir,'tmp/proposta-build/validation.json')}));
