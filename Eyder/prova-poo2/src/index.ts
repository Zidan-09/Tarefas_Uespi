import { DocumentManager } from "./services/documentManager";
import { Invoice } from "./services/invoice";
import { Report } from "./services/report";
import { DocumentType } from "./utils/documentType";

const Storage = new DocumentManager();

const doc_1: Report = new Report('Melhores Alunos', new Date(), '1', DocumentType.Report, "Todos");
const doc_2: Invoice = new Invoice('Pastel é saudável', new Date(), '1000', DocumentType.Invoice, "Não, pois seu alto índice de gordura promove a obesidade e o aumento do risco de infartos");
const doc_3: Report = new Report('Melhores Professores', new Date(), '2', DocumentType.Report, "Eyder Rios, Dário Calçada, Átila Rabelo, Francisco Rocha, Rodrigo Baluz");
const doc_4: Invoice = new Invoice('Filmes fracassados', new Date(), '2.50', DocumentType.Invoice, "Branca de neve - live action");
const doc_5: Report = new Report('NextJs é a melhor alternativa', new Date(), '3', DocumentType.Report, "Se você quer um design profissional e não quer ter dor de cabeça, essa é a melhor alternativa ");

Storage.add(doc_1);
Storage.add(doc_2);
Storage.add(doc_3);
Storage.add(doc_4);
Storage.add(doc_5);

console.log('Documents of Report type:\n');
console.log(Storage.search(DocumentType.Report));
console.log('\nDocuments of Invoice type:\n');
console.log(Storage.search(DocumentType.Invoice));

console.log('\nTudo detalhado:\n')

console.log(Storage.show());