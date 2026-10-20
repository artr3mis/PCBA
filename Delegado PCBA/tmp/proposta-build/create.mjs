import fs from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { Presentation, PresentationFile } from '@oai/artifact-tool';

const workspaceDir = 'C:/Users/Atr3mis/OneDrive/Documentos/Concursos/Delegado PCBA';
const build = path.join(workspaceDir, 'tmp/proposta-build');
const SKILL_DIR = 'C:/Users/Atr3mis/.codex/plugins/cache/openai-primary-runtime/presentations/26.1011.11113/skills/presentations';
const FINAL_PPTX = path.join(workspaceDir, 'output/Proposta de Honorarios Advocaticios.pptx');
const navy = '#182C3A', gold = '#A4814E', ivory = '#F7F4EE', ink = '#293C47', muted = '#62717A';
const p = Presentation.create({slideSize:{width:1280,height:720}});
function text(s, content, x,y,w,h,size=28,color=ink,bold=false){
 const t=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 t.text=content;
 t.text.style={fontSize:size,typeface:'Arial',color,bold,insets:0,autoFit:'none',verticalAlignment:'top',wrap:'square'};
 return t;
}
function slide(title,index,dark=false){
 const s=p.slides.add();s.background.fill=dark?navy:ivory;
 if(title) text(s,title,80,62,1100,76,44,dark?ivory:navy,true);
 text(s,String(index).padStart(2,'0'),1150,648,50,32,20,dark?'#C3B294':muted);
 return s;
}
let s=slide('',1,true);
text(s,'À [NOME DO CLIENTE]',80,70,1100,40,26,'#D4BE99');
text(s,'PROPOSTA DE\nHONORÁRIOS\nADVOCATÍCIOS',80,180,1120,230,60,ivory,true);
text(s,'Ação monitória',80,441,1080,55,32,'#D4BE99');
text(s,'Raimundo Santos Correia Filho',80,572,1060,40,28,ivory,true);
text(s,'Advogado – OAB/BA 83.020',80,619,1060,32,23,'#D4BE99');

s=slide('Objeto da atuação',2);
text(s,'Prezado(a) Senhor(a),',80,172,1090,40,28);
text(s,'Após análise preliminar da documentação apresentada, apresento proposta para atuação profissional visando ao ajuizamento de ação monitória contra a empresa devedora.',80,238,1060,170,30);
text(s,'CRÉDITO APROXIMADO',80,465,1060,40,23,gold,true);
text(s,'R$ 32.000,00',80,513,1060,100,64,navy,true);

s=slide('1. Serviços incluídos',3);
const services=['Análise e organização dos documentos','Elaboração e protocolo da ação monitória','Acompanhamento do processo em primeiro grau','Manifestações processuais ordinárias','Acompanhamento de eventual pagamento voluntário\nou apresentação de embargos monitórios'];
services.forEach((v,i)=>{text(s,String(i+1).padStart(2,'0'),80,176+i*84,58,50,27,gold,true);text(s,v,165,176+i*84,1025,78,28);});

s=slide('2. Honorários',4);
text(s,'A Tabela de Honorários da OAB-BA indica, como referência\npara o serviço, o valor de R$ 5.527,40.',80,161,1100,80,27,muted);
text(s,'Considerando as particularidades da contratação, proponho:',80,260,1120,45,26);
text(s,'R$ 3.000,00',80,331,550,92,61,navy,true);
text(s,'Honorários iniciais\nPagos na contratação',80,437,530,86,27);
text(s,'10%',735,331,430,92,68,navy,true);
text(s,'Honorários de êxito\nSobre o valor efetivamente recuperado',735,437,455,115,27);
text(s,'O êxito incidirá sobre todo valor recebido, por pagamento voluntário, acordo, bloqueio judicial, levantamento de valores ou qualquer outra forma de satisfação do crédito.',80,573,1110,80,23);
s.speakerNotes.text='Valor de referência da OAB-BA e condições conforme texto fornecido pelo proponente.';

s=slide('3. Despesas e serviços não incluídos',5);
text(s,'Custas e despesas',80,167,515,40,29,gold,true);
const costs=['Custas judiciais','Despesas de diligências','Taxas, certidões e emolumentos','Cópias, autenticações ou deslocamentos','Honorários de peritos ou profissionais auxiliares'];
costs.forEach((v,i)=>text(s,v,80,229+i*65,515,62,25));
text(s,'Atuação adicional',695,167,515,40,29,gold,true);
const extras=['Recursos para tribunais','Incidente de desconsideração da personalidade jurídica','Medidas executivas ou investigação patrimonial extraordinárias'];
extras.forEach((v,i)=>text(s,v,695,229+i*107,505,100,25));
text(s,'Eventuais despesas serão previamente comunicadas e correrão por conta do contratante.',80,611,1090,58,24,navy,true);

s=slide('4. Observação e formalização',6,true);
text(s,'A contratação não garante resultado específico, pois o êxito depende da análise judicial dos documentos, da defesa apresentada pela parte contrária e da existência de patrimônio penhorável.',80,178,1100,182,30,ivory);
text(s,'A presente proposta poderá ser formalizada mediante\ncontrato de honorários advocatícios próprio.',80,386,1100,93,29,'#D4BE99');
text(s,'Atenciosamente,',80,529,1100,38,23,ivory);
text(s,'Raimundo Santos Correia Filho',80,574,1100,45,30,ivory,true);
text(s,'Advogado – OAB/BA 83.020',80,625,1060,36,24,'#D4BE99');

await fs.mkdir(path.dirname(FINAL_PPTX),{recursive:true});
await fs.mkdir(build,{recursive:true});
for(let i=0;i<p.slides.items.length;i++){
 const blob=await p.export({slide:p.slides.items[i],format:'png',scale:1});
 await fs.writeFile(path.join(build,`slide-${i+1}.png`),new Uint8Array(await blob.arrayBuffer()));
}
const candidatePath=path.join(build,'candidate.pptx');
await (await PresentationFile.exportPptx(p)).save(candidatePath);
const {finalizePresentation}=await import(pathToFileURL(path.join(SKILL_DIR,'container_tools/artifact_tool_utils.mjs')).href);
const result=await finalizePresentation({workspaceDir,candidatePath,finalPath:FINAL_PPTX,
 pythonExecutable:'C:/Users/Atr3mis/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe',
 integrityValidatorPath:path.join(SKILL_DIR,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(SKILL_DIR,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit'],
 fontPolicy:{basis:'design',families:['Arial']},verifyArtifactToolImport:true,
 receiptPath:path.join(build,'validation.json')});
console.log(JSON.stringify(result));
