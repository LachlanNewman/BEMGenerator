class GenerateComponents:
        MAIN_DIRECTORY = './css'
        PAGE_DIRECTORY = MAIN_DIRECTORY + '/pages'
        COMPONENTS_DIRECTORY = MAIN_DIRECTORY + 'components'


        # def __init__(self):
        #     self.fileName
        #     self.html

        def getMainComponentList(self,html):
            return html.find_all('div', attrs={'data-component-main': True});

        def getComponentClass(self,component):
            className = str(component['class'])[2:-2]
            return className

        def concatAmpersand(self,className):
            className = className.replace(self.parentClass,'&')


        def getChildClasses(self, dom, classes : dict, childLevel : int):
            innerDOM = dom.find_all(attrs={'data-component-level-' + str(childLevel): True})
            if not dom:
                return classes
            else:
                for element in innerDOM:
                    parentClass = str(element['class'])[2:-2]
                    # childClass = self.getComponentClass(element)
                    childLevel = childLevel + 1
                    if parentClass not in classes.keys():
                        classes[parentClass] = self.getChildClasses(element,{},childLevel)
                    else:
                        classes[parentClass] = self.getChildClasses(element, classes[parentClass], childLevel)

                return classes

        def getClasses(self, html):
            classes = {}
            DOM = html.find_all('div', attrs={'data-component-main': True});
            if not html:
                return classes
            else:
                for element in DOM:
                    parentClass = str(element['class'])[2:-2]
                    # childClass = self.getComponentClass(element)
                    if parentClass not in classes:
                        # childClass = self.concatAmpersand(childClass)
                        # childList.append(childClass)
                        classes[parentClass] = self.getChildClasses(element, {}, 0)

                return classes