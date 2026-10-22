from pathlib import Path
import re, json

ROOT = Path(r'C:/Users/Atr3mis/OneDrive/Documentos/Concursos/Delegado PCBA')
VIS = Path(r'C:/Users/Atr3mis/.codex/visualizations/2026/10/04/01a106d7-d06a-7f41-8bac-561f29631896')
names = ['LÍNGUA PORTUGUESA','RACIOCÍNIO LÓGICO','ATUALIDADES','INFORMÁTICA','PROMOÇÃO DA IGUALDADE RACIAL E DE GÊNERO','MEDICINA LEGAL','LEGISLAÇÃO GERAL','DIREITO ADMINISTRATIVO','DIREITO CIVIL E EMPRESARIAL','DIREITO CONSTITUCIONAL','DIREITO PENAL','DIREITO PROCESSUAL PENAL','DIREITO PROCESSUAL CIVIL','DIREITO TRIBUTÁRIO','DIREITO AMBIENTAL','LEGISLAÇÃO PENAL E PROCESSUAL PENAL EXTRAVAGANTE','CRIMINOLOGIA']
text = (ROOT/'Conteudo-Delegado-Edital.md').read_text(encoding='utf-8')
text = re.sub(r'\[PAGINA \d+\]', '', text)
positions = [(name, text.index(name+':')) for name in names]
notes = {
0: ('Em estudo','Interpretação, inferência e extrapolação; coesão, referentes, conectivos e reescrita.','Iniciar gramática sistemática: sintaxe, concordância, regência, crase, pontuação e redação oficial.'),
4: ('Contato pontual','Representação e retratação na Lei Maria da Penha, dentro de Processo Penal.','Ainda não estudamos o programa de igualdade racial e de gênero de forma sistemática.'),
7: ('Em estudo','LIMPE; organização administrativa; órgãos e entidades; autarquias, fundações e empresas estatais; vinculação; elementos e vícios; introdução à anulação, revogação e convalidação.','Reforçar motivo × motivação e finalidade × objeto. Completar atos e iniciar os demais blocos.'),
9: ('Em estudo','Inviolabilidade domiciliar, área profissional não aberta ao público e fundamentos prévios para ingresso; art. 37 em diálogo com Administrativo.','Demais direitos fundamentais, remédios, segurança pública, organização do Estado e controle de constitucionalidade ainda pendentes.'),
10: ('Em estudo','Legalidade, anterioridade, retroatividade benéfica, abolitio criminis, leis temporárias e excepcionais; tempo e lugar do crime.','Iniciar teoria do crime; aprofundar lei penal no espaço. Parte especial, penas e prescrição pendentes.'),
11: ('Em estudo','Bloco básico de inquérito: características, instauração, representação, indiciamento, prazos, relatório, arquivamento e reabertura.','Completar sistemas e juiz das garantias, ação penal e ANPP; iniciar provas e prisões sistematicamente.'),
15: ('Contato pontual','Lei 12.830: indiciamento; Lei de Drogas: prazos; Lei Maria da Penha: representação/retratação.','Esses recortes não equivalem à conclusão das leis. As demais leis ainda não receberam estudo sistemático.')
}
mapping = {
0: {'1':('Parcial','Interpretação, inferência e extrapolação; tipologia, gêneros e funções da linguagem pendentes.'),'2':('Parcial','Sentidos e reescrita em exemplos; figuras, formação do repertório semântico e demais recortes pendentes.'),'4':('Contato pontual','Conectivos e relações entre orações em exercícios; sintaxe e demais subitens não estudados sistematicamente.'),'5':('Parcial','Reescrita para eliminar ambiguidade e manter sentido.'),'7':('Parcial','Referentes, pronomes, conectivos e relações de sentido.'),'8':('Contato pontual','Função de vocábulos em exemplos de interpretação.'),'10':('Contato pontual','Ajustes de registro e redação nas respostas; sem bloco específico de variação linguística.')},
4: {'7':('Contato pontual','Somente representação/retratação na Lei Maria da Penha; restante da lei e abordagem da disciplina pendentes.')},
7: {'1':('Parcial','Princípios expressos LIMPE e exemplos; regime e princípios implícitos pendentes.'),'2':('Parcial','Elementos, vícios, motivo/motivação; introdução à anulação, revogação e convalidação. Persistem confusões nas aplicações misturadas; maioria dos demais subitens pendente.'),'3':('Contato pontual','Hierarquia e vinculação; poderes disciplinar, regulamentar e de polícia ainda sem bloco próprio.'),'4':('Contato pontual','Concessão apenas como exemplo de descentralização por colaboração; serviços públicos não cobertos.'),'10':('Contato pontual','Tutela e controle finalístico; controle judicial e legislativo sem estudo sistemático.'),'15':('Parcial','Descentralização, desconcentração, órgãos e entidades praticados. Falta revisão posterior com questões oficiais inéditas.'),'16':('Parcial','Autarquias, fundações, empresas públicas e sociedades de economia mista; entidades paralelas pendentes.'),'17':('Parcial','Princípios expressos; supremacia, indisponibilidade e princípios implícitos pendentes.'),'20':('Contato pontual','Limites da atuação e hierarquia em casos, sem cobertura do bloco inteiro.'),'21':('Contato pontual','Desvio de finalidade e exemplos; poder regulamentar e deveres ainda pendentes.'),'25':('Parcial','Conceitos iniciais de anulação e revogação; falta aprofundar limites, efeitos e jurisprudência.')},
9: {'21':('Contato pontual','Fundamentos de garantias no inquérito e proteção domiciliar, sem teoria geral completa.'),'22':('Parcial','Art. 5º, XI e direitos do investigado; demais direitos pendentes.'),'23':('Contato pontual','Proteção domiciliar; demais direitos enumerados não estudados sistematicamente.'),'28':('Contato pontual','Silêncio e proteção domiciliar; demais garantias pendentes.'),'34':('Parcial','Art. 37: princípios e criação de entidades; demais regras constitucionais pendentes.')},
10: {'1':('Parcial','Legalidade e anterioridade; demais aspectos da introdução pendentes.'),'2':('Parcial','Lei no tempo e breve ligação ao lugar do crime. Territorialidade, extraterritorialidade, imunidades e concurso de normas pendentes.'),'3':('Parcial','Somente tempo e lugar do crime; teoria geral do crime ainda não estudada.'),'4':('Contato pontual','Extinção por abolitio criminis; não houve estudo de fato típico, dolo, culpa, erros e iter criminis.'),'9':('Contato pontual','Abolitio criminis; demais causas e prescrição pendentes.')},
11: {'1':('Contato pontual','Garantias do investigado e distinção entre investigação e processo. Sistemas, lei processual e juiz das garantias pendentes.'),'2':('Parcial','Inquérito, indiciamento, prazos, relatório, arquivamento e reabertura. Jurisdição, competência e incidentes do item 2.2 pendentes.'),'4':('Parcial','Espécies de ação para instauração, representação, retratação e decadência. ANPP e sujeitos processuais pendentes.'),'7':('Contato pontual','CPP 155, silêncio e ingresso domiciliar; teoria e meios de prova ainda sem cobertura sistemática.')},
15: {'16':('Contato pontual','Lei Maria da Penha: somente representação e retratação.'),'17':('Contato pontual','Lei de Drogas: somente prazos do inquérito e requisitos de duplicação.'),'22':('Contato pontual','Lei 12.830: indiciamento privativo e fundamentado; não se presume conclusão da lei.')}
}

disciplines=[]
for i,(name,start) in enumerate(positions):
    end=positions[i+1][1] if i+1<len(positions) else len(text)
    raw=text[start+len(name)+1:end]
    raw=re.split(r'CARGO: DELEGADO DE POLÍCIA CIVIL',raw)[0]
    raw=' '.join(raw.split())
    # Corrige somente separadores perdidos na extração, sem renumerar o edital.
    raw=re.sub(r'(?<=[A-Za-zÀ-ÿ])\.(?=\d{1,2}\.\s)', '. ', raw)
    raw=raw.replace('28 Lei Estadual', '28. Lei Estadual').replace('9 Teorias', '9. Teorias')
    matches=list(re.finditer(r'(?<![\d./])(\d{1,2})\.(?!\d)\s+',raw))
    items=[]
    occurrences={}
    for j,m in enumerate(matches):
        number=m.group(1)
        body=raw[m.end():matches[j+1].start() if j+1<len(matches) else len(raw)].strip()
        occurrences[number]=occurrences.get(number,0)+1
        status,evidence=mapping.get(i,{}).get(number,('Não iniciado','Sem estudo sistemático ou exercício específico registrado nesta conversa.'))
        items.append({'number':number,'occurrence':occurrences[number],'text':body,'status':status,'evidence':evidence})
    state,covered,nextstep=notes.get(i,('Não iniciado','Sem bloco de estudo registrado nesta conversa.','Iniciar os conteúdos listados abaixo, com teoria, lei quando pertinente e questões.'))
    disciplines.append({'name':name.title(),'group':'Comuns' if i<7 else 'Específicos','state':state,'covered':covered,'next':nextstep,'items':items})

evidence=[
 {'name':'Inquérito — bloco autoral de 10 objetivas','result':'9/10','limit':'Recorte básico e próximo da explicação; erro em indiciamento. Não mede todo Processo Penal.'},
 {'name':'Penal — 6 objetivas autorais de lei penal','result':'6/6','limit':'Lei penal, tempo e lugar; sem teoria do crime ou parte especial.'},
 {'name':'Português — dois blocos de 4 exercícios','result':'4/4 em cada','limit':'Interpretação, coesão e reescrita; amostras pequenas, com exercícios adaptados e autorais.'},
 {'name':'Simulado misto recente — 9 objetivas autorais','result':'9/9','limit':'Assuntos já ensinados; a discursiva teve núcleo correto, mas faltaram pontos do comando.'},
 {'name':'Vícios dos atos — exercícios misturados recentes','result':'Oscilação observada','limit':'Erros repetidos em motivo × motivação e finalidade × objeto, mesmo após acertos guiados.'},
 {'name':'Anulação, revogação e convalidação','result':'Introdução praticada','limit':'Houve troca de nome e omissão de requisitos; efeitos, limites e controle ainda não aprofundados.'},
]
pending=[
 'Motivo × motivação: explicação detalhada não torna verdadeiro um fato inexistente; motivação obrigatória ausente relaciona-se à forma.',
 'Finalidade × objeto: objetivo desviado (favorecimento/vingança) versus conteúdo jurídico determinado (multa acima do teto).',
 'Discursivas: responder todos os pontos do comando e justificar com o fato decisivo, evitando somente nomear o instituto.',
 'Criação de entidades: lei cria autarquia; lei autoriza empresa pública, sociedade de economia mista e fundação pública de direito privado.',
 'Representação: melhora nas últimas revisões, mas a condição não é substituída por prova suficiente ou requisição do MP.'
]
data={'date':'22/10/2026','disciplines':disciplines,'evidence':evidence,'pending':pending}
assert len(disciplines)==17
assert all(d['items'] for d in disciplines)
assert sum(d['state']=='Em estudo' for d in disciplines)==5
assert sum(d['state']=='Contato pontual' for d in disciplines)==2
assert sum(d['state']=='Não iniciado' for d in disciplines)==10
(ROOT/'output/painel-pcba-dados.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')

md=['# Painel de preparação — Delegado PCBA', '', '**Atualização:** 22/10/2026. **Fonte:** Edital.pdf local, Anexo I, transcrição em Conteudo-Delegado-Edital.md. **Evidência:** respostas desta conversa; estudo externo não informado não foi presumido.', '', '## Leitura do diagnóstico', '', '- 17 disciplinas: 5 com blocos estruturados iniciados; 2 somente com contatos pontuais; 10 sem estudo registrado.', '- Nenhuma disciplina integralmente concluída ou com domínio validado.', '- Não existe percentual confiável de cobertura/domínio: os itens do edital têm extensões diferentes e alguns se repetem.', '- Horas disponíveis: 5h/dia informadas. Horas efetivamente realizadas: não registradas. Não é possível calcular aderência ao plano.', '- Simulado integral de 100 questões, com tempo controlado: não registrado. Peça completa em condições de prova: não registrada.', '- O plano inicial previa ciclo mais amplo; a execução registrada concentrou-se em fundamentos de cinco disciplinas. É necessário ampliar a rotação, mantendo revisões curtas dos erros.', '', '## Comparação por disciplina', '', '| Disciplina | Situação | Evidência | Próximo passo |','|---|---|---|---|']
for d in disciplines: md.append(f"| {d['name']} | {d['state']} | {d['covered']} | {d['next']} |")
md+=['','## Resultados que podem ser usados como evidência','']
for e in evidence: md.append(f"- **{e['name']}: {e['result']}.** {e['limit']}")
md+=['','## Discursiva e demais etapas','','- Relatório de inquérito: houve tentativa e correções de estrutura/conclusão; não há peça completa validada no padrão do edital.', '- Casos: respostas curtas e um caso adaptado de prova oral; não há simulado completo com dois casos no padrão PCBA.', '- Prova objetiva local: 100 questões, 40 comuns + 60 específicas, mínimo 70. A tabela não permite presumir peso individual de cada disciplina.', '- Discursiva local: uma peça /60 e dois casos /20 cada, mínimo 70 no total; nenhuma nota completa aferida.', '- TAF, exames médicos, avaliação psicológica, investigação social, títulos e curso de formação: sem acompanhamento de execução registrado neste chat.', '- Inscrição: confirmada pelo usuário. Datas e demais atos exigem conferência nas publicações oficiais quando forem utilizados para decisões.','','## Prioridades de ajuste','']
for p in pending: md.append('- '+p)
md+=['','- Encerrar a revisão imediata dos vícios com poucas questões e voltar a eles em revisões posteriores; evitar consumir todo o ciclo em um único assunto.', '- Alternar os blocos centrais Penal/Processo Penal/Constitucional/Administrativo com disciplinas ainda não iniciadas; incluir comuns e leis baianas no ciclo.', '- Ampliar questões oficiais inéditas, registrar dúvida e tempo, e corrigir sem converter respostas guiadas em indicador de aprovação.', '- Evoluir para escrita completa com limite de linhas e tempo; registrar horas reais antes de recalcular a carga restante.','','## Inventário integral do edital e situação de cada item','','A numeração e eventuais repetições foram preservadas da transcrição. Subitens permanecem dentro do item principal. “Parcial” não significa que todos os subitens foram estudados. O texto de referência é o PDF original.']
for d in disciplines:
    md+=['',f"### {d['name']}",'']
    for it in d['items']:
        md += [f"**{it['number']}. {it['text']}**",'',f"Situação: **{it['status']}**. {it['evidence']}",'']
(ROOT/'Painel-PCBA-2026-10-22.md').write_text('\n'.join(md),encoding='utf-8')
template=(ROOT/'output/painel-modelo.html').read_text(encoding='utf-8')
result=template.replace('__DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/'))
assert '__DATA__' not in result
(VIS/'painel-pcba.html').write_text(result,encoding='utf-8')
print(json.dumps({'disciplinas':len(disciplines),'itens_principais':sum(len(d['items']) for d in disciplines),'por_disciplina':[(d['name'],len(d['items'])) for d in disciplines],'html_bytes':len(result.encode()),'report':str(ROOT/'Painel-PCBA-2026-10-22.md')},ensure_ascii=False))
