export const calculateNumber = (type,a,b)=>{

    a = Math.round(a)
    b = Math.round(b)

    switch (type) {
        case "SUM":
            return Math.ceil(a+b);
        break;
        case "SUBTRACT":
            return a-b;
        break;
        case "DIVIDE":

            if(b === 0){
                return "Error";
            }

            return a/b;
        break;
    
        default:
            new Error('Parameter value is not valide');
        break;
    }
}
