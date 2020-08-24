function Node(value){

    this.value = value;
    this.next = null;
}

function LinkedList(){
    
    this.first = null;
    this.push = LinkedListPush;
    this.pop = LinkedListPop;
    this.print = LinkedListPrint;
    this.lenght = LinkedListLenght;
}

    function LinkedListPush(value, position){

        if(!this.first){

            this.first = new Node(value);
            return true;
        }

        count = 0;
        current = this.first;

        if(position == count){

            this.first = new Node(value);
            this.first.next = current
            return true;
        }

        before = this.first;
        current = this.first.next;

        while(before){

            count += 1;

            if(count == position){

                before.next = new Node(value);
                before.next.next = current;
                return true;
            }

            before = before.next;
            current = current.next;
        }

        current = new Node(value);
        return true;
    }

    function LinkedListPop(position){

        before = this.first;
        current = this.first.next;
        count = 0;

        if(position == 0){

            this.first = before.next;
        }

        while(current){

            count += 1;

            if(position == count){

                before.next = before.next.next;

                return true;
            }

            before = before.next;
            current = current.next;
        }
    }

    function LinkedListPrint(){

        current = this.first;
        str =" ";

        while(current){
            
            str +=`${current.value}=>`;
            current = current.next;

        }

        str += " null";

        return str;
    }

    function LinkedListLenght(){

        current = this.first;
        count = 0;

        while(current){
            count += 1;
            current = current.next;
        }

        return count;
    }