import { DocumentContract } from "../entities/documentContract";
import { DocumentType } from "../utils/documentType";

export class DocumentManager<T extends DocumentContract> {
    private documents: T[] = [];

    add(document: T) {
        this.documents.push(document);
    };

    search(type: DocumentType): T[] {
        let documents: T[] = [];

        for (let i of this.documents) {
            if (i.type === type) {
                documents.push(i);
            }
        }

        return documents;
    };

    show() {
        let contents: string[] = []
        for (let i of this.documents) {
            const content = i.getContent().split('-');
            const formated = content[0].padEnd(30, ' ') + '------' + content[1];

            contents.push(formated);
        }
        return contents;
    }
}