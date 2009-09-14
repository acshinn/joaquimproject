from PyQt4.QtOpenGL import *
from PyQt4.QtGui import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.raw.GLUT import *

from objects import *

class GlWidget(QGLWidget):
	"""Our implementation of QGLWidget widget. :) - Joaquim, el gato."""
	
	def __init__ (self, parent=None):
		"""Constructor"""
		
		super(GlWidget, self).__init__(parent)
		#Para que o movimento do mouse seja reconhecido sem se pressionar nenhum botao do mouse
		self.setMouseTracking(True)
		
		self.sceneObjects = []
		self.selectedObject = None
		#self.boundingSphere = Sphere(radius, wire)
		self.mousePosX = 0.0
		self.mousePosY = 0.0
		self.mousePosZ = 0.0
		
	def paintGL(self):
		"""A Simple drawing callback for drawing one triangle"""
		
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		#glRotate(2, 0.5, 0.9, 0.5)
		self.render()
		#self.drawing()
		
#	def selection(self):
#		glLoadName(1)
#		Cube(0.5)
#		
#		glLoadName(2)
#		Sphere(0.5)
#		
#		hits = glRenderMode(GL_RENDER)
#		print "Hits = ", hits
#	
#	def drawing(self):
#		Cube(0.5)
#		Sphere(0.5)
#		
#	def picking(self):
#		viewport = glGetIntegerv(GL_VIEWPORT)
#		print "Viewport = ", viewport
#		print "Viewport[3] = ", viewport[3]
#		
#		glSelectBuffer(512)
#		glRenderMode(GL_SELECT)
#		
#		glInitNames()
#		glPushName(0)
#		
#		glMatrixMode(GL_PROJECTION)
#		glPushMatrix()
#		glLoadIdentity()
#		
#		gluPickMatrix(QCursor.pos().x(), viewport[3] - QCursor.pos().y(),
#					  5.0, 5.0, viewport)
#		
#		gluPerspective(45, 1.3, 10, 40)
#		
#		self.selection()
#		glMatrixMode(GL_PROJECTION)
#		glPopMatrix()
#		glFlush()

	def resizeGL (self, width, height):
		"""A simple resize callback."""
		
		side = min(width,height)
		glViewport((width - side) / 2, (height - side) / 2, side, side)
		glMatrixMode(GL_MODELVIEW)

	def mouseMoveEvent(self, ev):
		self.updateMousePosition()
		self.update()
		
	def mousePressEvent(self, ev):
#		print "Clico! ;D"
#		self.picking()
		print "Type:", ev.type()
#		
	def mouseReleaseEvent(self, ev):
		print "Solto... :("			 

<<<<<<< .mine    def keyPressEvent(self, ev):
        key = str(ev.text()).upper()
        if (key == "C"):
            self.cube = True
            self.update()
        elif (key == "E"):
            self.sphere = True
            self.update()
        else:
            pass        
    
    def draw(self):
        self.mousePosX = self.mapFromGlobal(QCursor.pos()).x()
        self.mousePosY = self.mapFromGlobal(QCursor.pos()).y()
        
#        self.mousePosZ = glReadPixels(self.mousePosX, self.mousePoxY, 1, 1, 
#                                      GL_DEPTH_COMPONENT, GL_FLOAT)
        self.mousePosZ = 1
        
        #Para que o movimento do mouse seja reconhecido sem se pressionar nenhum botao do mouse
        self.setMouseTracking(True)
=======	def enterEvent(self, ev):
		self.setFocus()
		self.grabKeyboard()
		
	def leaveEvent(self, ev):
		self.parent().setFocus()
		self.releaseKeyboard()
>>>>>>> .theirs
	def keyPressEvent(self, ev):
		key = str(ev.text()).upper()
		if (key == "C"):
			newCube = Cube(0.5)
			newCube.setCentralPosition(self.getMouseScenePosition())
			self.sceneObjects.append(newCube)
			self.update()
		elif (key == "E"):
			newSphere = Sphere(0.5)
			newSphere.setCentralPosition(self.getMouseScenePosition())
			self.sceneObjects.append(newSphere)
			self.update()
		else:
			pass
		
	def updateMousePosition(self):
		self.mousePosX = self.mapFromGlobal(QCursor.pos()).x()
		self.mousePosY = self.mapFromGlobal(QCursor.pos()).y()
			
	def getMouseScenePosition(self):
		self.mousePosZ = glReadPixels(self.mousePosX, self.mousePosY, 1, 1, 
									  GL_DEPTH_COMPONENT, GL_FLOAT)
		#self.mousePosZ = 0.1

		adjustedY = glGetIntegerv(GL_VIEWPORT)[3] - self.mousePosY - 1
		
		self.coordPosition = gluUnProject(self.mousePosX, adjustedY, self.mousePosZ,
										  glGetDoublev(GL_MODELVIEW_MATRIX),
										  glGetDoublev(GL_PROJECTION_MATRIX),
										  glGetIntegerv(GL_VIEWPORT))
		
		return self.coordPosition
		
	def render(self):
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glColor3f(1.0, 0, 0)
		for obj in self.sceneObjects:
			glPushMatrix()
			obj.render()
			glPopMatrix()
		