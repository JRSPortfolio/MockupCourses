'use strict';

////////////////////////////////////////////////////////////////////////
//
//      EXEMPLOS INTRODUTÓRIOS: CONCAT e SPLICE
//
////////////////////////////////////////////////////////////////////////

function concat01(items){
    const itemsTxt = [];
    for (let item of items) {
        itemsTxt.push(item.toString());
    }
    return itemsTxt.join('');
}

function concat02(...items){
    const itemsTxt = [];
    for (let item of items) {
        itemsTxt.push(item.toString());
    }
    return itemsTxt.join('');
}

