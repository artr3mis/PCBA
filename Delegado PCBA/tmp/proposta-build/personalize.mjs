import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {FileBlob, PresentationFile} from '@oai/artifact-tool';
process.env.RUNTIME_NODE_MODULES='C:/Users/Atr3mis/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const workspaceDir='C:/Users/Atr3mis/OneDrive/Documentos/Concursos/Delegado PCBA';
const skill='C:/Users/Atr3mis/.codex/plugins/cache/openai-primary-runtime/presentations/26.1011.11113/skills/presentations';
const p=await PresentationFile.importPptx(await FileBlob.load(path.join(workspaceDir,'output/Proposta de Honorarios Advocaticios.pptx')));
const s=p.slides.items[0];
const inspected=await p.inspect({kind:'textbox',search:'NOME DO CLIENTE',maxChars:10000});
const target=inspected.ndjson.split('\n').filter(Boolean).map(x=>JSON.parse(x)).find(x=>x.kind==='textbox' && x.text==='À [NOME DO CLIENTE]');
if(!target) throw new Error('Campo do cliente não localizado');
p.resolve(target.id).text='À JULIANA BELLAS PRADO BARQUEIRO';
const logo=await fs.readFile('C:/Users/Atr3mis/Downloads/Captura de tela 2026-10-13 205546.png');
s.images.add({blob:logo,contentType:'image/png',alt:'Correia Filho Advocacia',fit:'contain',position:{left:855,top:225,width:280,height:280}});
const closing=p.slides.items[5];
closing.images.add({blob:logo,contentType:'image/png',alt:'Correia Filho Advocacia',fit:'contain',position:{left:1010,top:535,width:140,height:140}});
const preview=await p.export({slide:s,format:'png',scale:1});
await fs.writeFile(path.join(workspaceDir,'tmp/proposta-build/logo-cover.png'),new Uint8Array(await preview.arrayBuffer()));
const lastPreview=await p.export({slide:closing,format:'png',scale:1});
await fs.writeFile(path.join(workspaceDir,'tmp/proposta-build/logo-closing.png'),new Uint8Array(await lastPreview.arrayBuffer()));
const candidatePath=path.join(workspaceDir,'tmp/proposta-build/logo-candidate.pptx');
await (await PresentationFile.exportPptx(p)).save(candidatePath);
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const result=await finalizePresentation({workspaceDir,candidatePath,
 finalPath:path.join(workspaceDir,'output/Proposta Juliana Bellas Prado Barqueiro - Correia Filho Advocacia.pptx'),
 pythonExecutable:'C:/Users/Atr3mis/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit'],
 fontPolicy:{basis:'design',families:['Arial']},verifyArtifactToolImport:true,
 receiptPath:path.join(workspaceDir,'tmp/proposta-build/logo-validation.json')});
console.log(result.finalPath);
