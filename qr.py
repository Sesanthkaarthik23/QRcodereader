import cv2

# Function to process QR code
def process_qr_code(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    qr_decoder = cv2.QRCodeDetector()
    _, decoded_info, _, _ = qr_decoder.detectAndDecodeMulti(gray)
    return decoded_info

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect and process QR codes
    qr_data = process_qr_code(frame)
    if qr_data is not None:  # Check if qr_data is not None
        cv2.putText(frame, str(qr_data), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("QR Code Scanner", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()