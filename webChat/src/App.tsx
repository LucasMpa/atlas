import { useState } from "react";
import { askQuestion, uploadDocument } from "./api";
import type { UploadedDocument } from "./api";
import type { ChatMessage } from "./types";
import Header from "./components/Header";
import UploadPanel from "./components/UploadPanel";
import ChatPanel from "./components/ChatPanel";

function App() {
  const [uploadedDoc, setUploadedDoc] = useState<UploadedDocument | null>(null);
  const [uploading, setUploading] = useState(false);
  const [uploadError, setUploadError] = useState<string | null>(null);

  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [asking, setAsking] = useState(false);
  const [chatError, setChatError] = useState<string | null>(null);

  async function handleUpload(file: File) {
    setUploading(true);
    setUploadError(null);

    try {
      const doc = await uploadDocument(file);
      setUploadedDoc(doc);
    } catch (err) {
      setUploadError(err instanceof Error ? err.message : "Falha no upload");
    } finally {
      setUploading(false);
    }
  }

  async function handleAsk(question: string) {
    setMessages((prev) => [...prev, { role: "user", content: question }]);
    setAsking(true);
    setChatError(null);

    try {
      const answer = await askQuestion(question);
      setMessages((prev) => [...prev, { role: "assistant", content: answer }]);
    } catch (err) {
      setChatError(err instanceof Error ? err.message : "Algo deu errado");
    } finally {
      setAsking(false);
    }
  }

  return (
    <>
      <Header />
      <main className="w-full pt-16 bg-surface min-h-screen">
        <div className="flex flex-col w-full h-[calc(100vh-64px)] overflow-hidden mx-auto max-w-2xl">
          <UploadPanel
            uploadedDoc={uploadedDoc}
            uploading={uploading}
            error={uploadError}
            onUpload={handleUpload}
          />
          <ChatPanel
            hasDocument={uploadedDoc !== null}
            messages={messages}
            asking={asking}
            error={chatError}
            onSend={handleAsk}
          />
        </div>
      </main>
    </>
  );
}

export default App;
