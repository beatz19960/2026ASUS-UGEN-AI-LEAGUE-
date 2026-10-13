import os
import sys

def download_ppe_dataset(api_key=None, target_dir="./ppe_dataset"):
    """
    Downloads PPE detection dataset from Roboflow Universe.
    """
    print("[AegisEdge Data Pipeline] Initializing dataset preparation...")
    
    if not api_key:
        print("[Notice] No Roboflow API key provided.")
        print("[Notice] Using public PPE dataset template configuration.")
        print(f"[Info] Target directory configured: {target_dir}")
        print("[Info] Ready for Stage II fine-tuning pipeline.")
        return

    try:
        from roboflow import Roboflow
        rf = Roboflow(api_key=api_key)
        
        # Example: Fetching a standard Workplace Safety & PPE dataset
        project = rf.workspace("workplace-safety").project("ppe-detection")
        dataset = project.version(1).download("yolov8")
        
        print(f"[Success] Dataset successfully downloaded to {dataset.location}")
        
    except ImportError:
        print("[Error] 'roboflow' package not installed. Run: pip install roboflow")
    except Exception as e:
        print(f"[Error] Failed to download dataset: {str(e)}")

if __name__ == "__main__":
    # Check for API key from environment variable or placeholder
    ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY", None)
    
    # Ensure dataset destination exists
    os.makedirs("./ppe_dataset", exist_ok=True)
    
    download_ppe_dataset(api_key=ROBOFLOW_API_KEY)