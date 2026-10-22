const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const base = 'C:/Users/Atr3mis/OneDrive/Documentos/Concursos/Delegado PCBA';
const html = fs.readFileSync('C:/Users/Atr3mis/.codex/visualizations/2026/10/04/01a106d7-d06a-7f41-8bac-561f29631896/painel-pcba.html','utf8');
const script = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)][0][1];
new vm.Script(script);
console.log('JavaScript: sintaxe válida.');
const data=JSON.parse(fs.readFileSync(path.join(base,'output/painel-pcba-dados.json'),'utf8'));
if(data.disciplines.length!==17)throw Error('Número de disciplinas');
console.log('Disciplinas: 17; itens: '+data.disciplines.reduce((a,d)=>a+d.items.length,0));
(async()=>{
  const {chromium}=require('C:/Users/Atr3mis/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
  const browser=await chromium.launch({headless:true,channel:'msedge'});
  const page=await browser.newPage();
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('file:///'+path.join(base,'output/painel-preview.html').replaceAll('\\','/'));
  const frame=page.frameLocator('iframe');
  await frame.locator('#pcba-subject').waitFor();
  for(const width of [736,360]){
    await page.setViewportSize({width,height:1000});
    await frame.locator('#pcba-subject').selectOption('0');
    if(await frame.locator('#pcba-items details').count()!==10)throw Error('Seleção não atualiza');
    await frame.locator('#pcba-subject').selectOption('7');
    await frame.locator('#pcba-items summary').first().click();
    const overflow=await frame.locator('#pcba-audit').evaluate(el=>el.scrollWidth>el.clientWidth+2);
    if(overflow)throw Error('Transbordamento em '+width);
    await page.screenshot({path:path.join(base,'output/painel-'+width+'.png'),fullPage:true});
    console.log('Navegação e layout: '+width+'px OK');
  }
  if(errors.length)throw Error(errors.join('\n'));
  await browser.close();
})().catch(e=>{console.error(String(e));process.exitCode=1});
