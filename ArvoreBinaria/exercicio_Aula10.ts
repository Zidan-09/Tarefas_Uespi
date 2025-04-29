class item {
    value: number;
    left: null | item;
    right: null | item;

    constructor(value: number) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class tree {
    NoRaiz: null | item;
    quantidade: number;

    constructor() {
        this.NoRaiz = null;
        this.quantidade = 0;
    }

    quantidadeItens() {
        console.log('A árvore contém:', this.quantidade, 'itens!')
    };

    maior() {
        let find: Boolean = false;
        let maior: null | item = this.NoRaiz;
        if (maior?.right == null) {
            console.log('O maior é', maior!.value);
        } else {
            while (!find) {
                find = true;
                if (maior!.right == null) {
                    console.log('O maior é', maior!.value);
                } else {
                    maior = maior!.right;
                    find = false;
                }
            }
        }
    };

    menor() {
        let find: Boolean = false;
        let menor: null | item = this.NoRaiz;
        if (menor?.left == null) {
            console.log('O menor é', menor!.value);
        } else {
            while (!find) {
                find = true;
                if (menor!.left == null) {
                    console.log('O menor é', menor!.value);
                } else {
                    menor = menor!.left;
                    find = false;
                }
            }
        }
    };

    soma() {
        let total: number = 0;
        let temp: item = this.NoRaiz!;
        let foi: number[] = [];

        for (let i = 0; i < this.quantidade; i++) {
            if (temp.left != null && temp.left!.value in foi) {
                temp = temp.left;
            } else if (temp.left != null && temp.left!.value in foi) {
                total += temp.left!.value;
                foi.push(temp.left!.value);
                temp = temp.left;
            } else if (temp.right != null && temp.right!.value in foi) {
                temp = temp.right;
            } else if (temp.right != null && temp.right!.value in foi) {
                total += temp.right!.value;
                foi.push(temp.right!.value);
                temp = temp.right;
            }
        }
        console.log('Soma:', total);
    };

    adicionar(item: item) {
        this.quantidade++;
        if (this.NoRaiz == null) {
            this.NoRaiz = item;
        } else {
            let done: Boolean = false;
            while (!done) {
                done = true;
                let temp: item = this.NoRaiz;
                if (item.value < temp.value!) {
                    if (temp.left == null) {
                        temp.left = item;
                    } else {
                        temp = temp.left;
                    }
                } else {
                    if (temp.right == null) {
                        temp.right = item;
                    } else {
                        temp = temp.right;
                    }
                }
            }
        }
    }
}

const arvore: tree = new tree();

const i1: item = new item(5);
const i2: item = new item(7);
const i3: item = new item(6);
const i4: item = new item(2);
const i5: item = new item(3);
const i6: item = new item(10);

arvore.adicionar(i1);
arvore.adicionar(i2);
arvore.adicionar(i3);
arvore.adicionar(i4);
arvore.adicionar(i5);
arvore.adicionar(i6);

arvore.maior();
arvore.menor();
arvore.quantidadeItens();
arvore.soma();