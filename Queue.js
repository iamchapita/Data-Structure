function Queue(){
    
    this.first=null;
    this.push=QueuePush;
    //this.print=QueuePrint;
    //this.pop=QueuePop;

}

    function QueuePush(value){

        if(!this.first){
            
            this.first= new Node(value);

        }else{

            current=this.first;
            while(current.next){

                current=current.next;

            }

            current.next= new Node(value);

        }

    }

function Node(value){

    this.value=value;
    this.next=null;
    

}
    /*function QueuePrint(){

        string="";
        current=this.first;

        while(current){

            string+=`${current.value} => `;
            current=current.next;

        }
        string+="null";
        return string;}*/
        