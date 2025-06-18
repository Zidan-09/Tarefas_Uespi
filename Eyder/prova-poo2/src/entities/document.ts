import { DocumentType } from "../utils/documentType";
import { DocumentContract } from "./documentContract";

export abstract class Document implements DocumentContract {
    private title: string;
    private date: Date;
    private content: string;
    type: DocumentType

    constructor(title: string, date: Date, type: DocumentType, content: string) {
        this.title = title;
        this.date = date;
        this.type = type;
        this.content = content;
    }

    getContent(): string {
        return `${this.title} - ${this.content}`;
    };
}