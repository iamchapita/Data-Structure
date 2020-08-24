function BSTNode(value) {

    this.value = value;
    this.left = null;
    this.right = null;

}




function BST(){
    this.root=null;
    this.add=BSTAdd;
    this.convert=BSTConvert;
    this.search=BSTSearch;
}
function BSTNode(value){
    this.value=value;
    this.left=null;
    this.right=null;
}
function BSTAdd(value,current=this.root){
    if (!this.root){
        this.root=new BSTNode(value);
        return true;
    }
    if (current.value > value){
        if (!current.left){
            current.left =new BSTNode(value);
            return true;
        }
    return this.add(value, current.left);
    }else
    if (current.value<value){
        if (!current.right){
            current.right= new BSTNode(value);
            return true;
        }
    return this.add(value, current.right);
    }
    return false;
}
function BSTConvert(LL){
    if (LL instanceof LinkedList){
        var current=LL.first;
        while(current){
            var value=current.value;
            this.add(value);
            current=current.next;
        }
        return true;
    }
    return false;
}
function BSTSearch(value, current=this.root){
    if (!this.root){
        return false;
    }
    if (current.value==value){
        return true;
    }else
    if (current.value>value){
        if(!current.left){
            return false;
        }
    return this.search(value,current.right);
    }
}