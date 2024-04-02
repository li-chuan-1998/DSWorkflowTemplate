import matplotlib.pyplot as plt

from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay


def draw_cm(y_test, y_pred, classes):
    cm = confusion_matrix(y_test, y_pred, labels=classes)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classes)
    disp.plot()
    plt.show()
    
def get_eval_res(y_test, y_pred, classes):
    draw_cm(y_test, y_pred, classes)
    print("Overall Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))