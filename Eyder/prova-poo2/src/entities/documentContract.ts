import { DocumentType } from "../utils/documentType";

export interface DocumentContract {
    type: DocumentType;
    getContent(): string;
}