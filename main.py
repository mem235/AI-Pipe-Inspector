import cv2

class PipeInspector:
    """
    AI-powered system for autonomous pipeline defect detection.
    Designed for industrial maintenance and robotic inspection.
    """
    def __init__(self):
        # Initialize the camera (0 is default camera)
        self.camera = cv2.VideoCapture(0)
        self.is_running = True

    def process_frame(self, frame):
        """
        Processes the camera frame to identify structural defects like cracks.
        """
        # Convert to Grayscale for easier processing
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply Canny Edge Detection to highlight anomalies
        edges = cv2.Canny(gray, 100, 200)
        
        return edges

    def run_inspection(self):
        """
        Starts the real-time inspection loop.
        """
        print("Inspection System Started... Press 'q' to quit.")
        
        while self.is_running:
            ret, frame = self.camera.read()
            if not ret:
                print("Failed to grab frame. Exiting...")
                break
            
            # Detect defects
            defects = self.process_frame(frame)
            
            # Display results
            cv2.imshow('Robot View - Original', frame)
            cv2.imshow('Defect Detection View', defects)
            
            # Quit if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.is_running = False

        self.camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    inspector = PipeInspector()
    inspector.run_inspection()
