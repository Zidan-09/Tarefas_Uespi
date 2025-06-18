import { Document } from '../entities/document'
import { DocumentType } from '../utils/documentType';

export class Report extends Document {
    analiseSession: string;

    constructor(title: string, date: Date, analiseSession: string, type: DocumentType, content: string) {
        super(title, date, type, content);
        this.analiseSession = analiseSession;
    }
}