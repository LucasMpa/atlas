import { useRef, useState, type DragEvent } from "react";
import type { UploadedDocument } from "../api";

interface UploadPanelProps {
  uploadedDoc: UploadedDocument | null;
  uploading: boolean;
  error: string | null;
  onUpload: (file: File) => void;
}

function UploadPanel({ uploadedDoc, uploading, error, onUpload }: UploadPanelProps) {
  const [isDragging, setIsDragging] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  function handleDragOver(event: DragEvent<HTMLDivElement>) {
    event.preventDefault();
    setIsDragging(true);
  }

  function handleDragLeave(event: DragEvent<HTMLDivElement>) {
    event.preventDefault();
    setIsDragging(false);
  }

  function handleDrop(event: DragEvent<HTMLDivElement>) {
    event.preventDefault();
    setIsDragging(false);
    const file = event.dataTransfer.files?.[0];
    if (file) onUpload(file);
  }

  function handleFileSelected(file: File | undefined) {
    if (file) onUpload(file);
  }

  return (
    <div className="h-[30%] bg-surface flex flex-col items-center justify-center p-md relative overflow-hidden border-b border-outline-variant/10 shrink-0">
      <div className="absolute inset-0 pointer-events-none opacity-20">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-primary/20 rounded-full blur-[120px]" />
        <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-secondary/10 rounded-full blur-[100px]" />
      </div>

      <div
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        onClick={() => !uploading && inputRef.current?.click()}
        className={`relative z-10 w-full max-w-2xl bg-surface-container-low rounded-xl p-md flex flex-col items-center justify-center text-center shadow-xl hover:shadow-2xl transition-shadow duration-300 group cursor-pointer border transition-colors h-full ${
          isDragging ? "border-primary bg-surface-container" : "border-outline-variant/20 hover:border-primary/50"
        }`}
      >
        <input
          ref={inputRef}
          type="file"
          accept="application/pdf"
          className="hidden"
          onChange={(e) => handleFileSelected(e.target.files?.[0])}
        />

        {uploadedDoc ? (
          <>
            <div className="w-12 h-12 mb-sm rounded-full bg-primary/10 flex items-center justify-center border border-primary/20">
              <span className="material-symbols-outlined text-2xl text-primary">
                description
              </span>
            </div>
            <h2 className="font-headline-md text-headline-md text-on-surface mb-xs">
              Documento carregado
            </h2>
            <p className="font-body-sm text-body-sm text-on-surface-variant mb-md max-w-[28rem]">
              {uploadedDoc.filename}
            </p>
          </>
        ) : (
          <>
            <div className="w-12 h-12 mb-sm rounded-full bg-surface-container-high flex items-center justify-center group-hover:bg-primary/10 transition-colors duration-300">
              <span className="material-symbols-outlined text-2xl text-on-surface-variant group-hover:text-primary transition-colors duration-300">
                cloud_upload
              </span>
            </div>
            <h2 className="font-headline-md text-headline-md text-on-surface mb-xs">
              {uploading ? "Enviando..." : "Solte o PDF aqui"}
            </h2>
            <p className="font-body-sm text-body-sm text-on-surface-variant mb-md max-w-[28rem]">
              Envie um documento para começar a conversa.
            </p>
            <button
              type="button"
              disabled={uploading}
              onClick={(e) => {
                e.stopPropagation();
                inputRef.current?.click();
              }}
              className="bg-primary text-on-primary font-label-md text-label-md px-md py-sm rounded-lg flex items-center gap-sm hover:brightness-110 transition-all focus:outline-none focus:ring-2 focus:ring-primary/50 focus:ring-offset-2 focus:ring-offset-surface disabled:opacity-50"
            >
              <span className="material-symbols-outlined text-[16px]">
                folder_open
              </span>
              Selecionar arquivo
            </button>
          </>
        )}
      </div>

      {uploading && (
        <div className="absolute top-0 left-0 w-full h-[2px] bg-surface-container-high z-50">
          <div className="h-full bg-primary w-1/3 animate-pulse" />
        </div>
      )}

      {error && (
        <p className="absolute bottom-2 text-label-sm font-label-sm text-error z-10">
          {error}
        </p>
      )}
    </div>
  );
}

export default UploadPanel;
