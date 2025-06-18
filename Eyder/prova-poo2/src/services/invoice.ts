import { Document } from '../entities/document';
import { DocumentType } from '../utils/documentType';

export class Invoice extends Document {
    totalValue: string;

    constructor(title: string, date: Date, totalValue: string, type: DocumentType, content: string) {
        super(title, date, type, content);
        this.totalValue =  totalValue;
    }
}