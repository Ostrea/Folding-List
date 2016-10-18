var treeMenu = {};

treeMenu.createTree = function (id) {
    var ulTags = document.getElementById(id).getElementsByTagName("ul");
    for (var i = 0; i < ulTags.length; i++)
        treeMenu.buildSubTree(id, ulTags[i], i);
};

treeMenu.buildSubTree = function (id, ulElement, index) {
    ulElement.parentNode.className = "submenu";

    // If ul has no status attribute explicitly added by user.
    if (ulElement.getAttribute("status") === null ||
        ulElement.getAttribute("status") === false) {

        ulElement.setAttribute("status", "closed");
    }
    // Else if this ul has an explicit status value of "opened".
    else if (ulElement.getAttribute("status") === "opened") {
        // Expand this ul plus all parent uls, so the most inner ul is revealed.
        treeMenu.expandSubTree(id, ulElement);
    }

    ulElement.parentNode.onclick = function (event) {
        var subMenu = this.getElementsByTagName("ul")[0];

        if (subMenu.getAttribute("status") === "closed") {
            subMenu.style.display = "block";
            subMenu.setAttribute("status", "opened");
        } else if (subMenu.getAttribute("status") === "opened") {
            subMenu.style.display = "none";
            subMenu.setAttribute("status", "closed");
        }
        treeMenu.preventPropagation(event);
    };

    ulElement.onclick = function (event) {
        treeMenu.preventPropagation(event);
    };
};

// Expand a ul element and any of its parent uls.
treeMenu.expandSubTree = function (id, ulElement) {
    var rootNode = document.getElementById(id);
    var currentNode = ulElement;
    currentNode.style.display = "block";
    while (currentNode !== rootNode) {
        // If parent node is a ul, expand it too.
        if (currentNode.tagName === "ul") {
            currentNode.style.display = "block";
            currentNode.setAttribute("status", "opened");
        }
        currentNode = currentNode.parentNode;
    }
};

////A few utility functions below//////////////////////

// Prevent action from bubbling upwards.
treeMenu.preventPropagation = function (event) {
    if (typeof e !== "undefined") {
        event.stopPropagation();
    } else {
        event.cancelBubble = true;
    }
};

document.addEventListener("DOMContentLoaded", function () {
    treeMenu.createTree("super_menu");
});